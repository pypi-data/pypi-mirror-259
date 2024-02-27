

import pandas as pd
import numpy as np
from scipy.spatial import cKDTree
import tifffile as tiff
from tqdm import tqdm
from scipy import ndimage
from matplotlib import pyplot as plt
import os
from PIL import Image


#
def MakeImages(path_to_spatial, spatial_sample_name, method, mode, path_to_network,network_name,
                overlap, block_size, r, inputvalue, fill, outputimageformat):
    
    # make output folders
    if not os.path.isdir('./Results/02. Mapping/'):
        os.mkdir('./Results/02. Mapping/')
    if not os.path.isdir('./Results/02. Mapping/' + spatial_sample_name):
        os.mkdir('./Results/02. Mapping/' + spatial_sample_name)
    if not os.path.isdir('./Results/02. Mapping/' + spatial_sample_name + '/clusters/'):
        os.mkdir('./Results/02. Mapping/' + spatial_sample_name + '/clusters/')
    if not os.path.isdir('./Results/02. Mapping/' + spatial_sample_name + '/genes/'):
        os.mkdir('./Results/02. Mapping/' + spatial_sample_name + '/genes/')
        
    
    # Load the stereoseq CSV file (gem file) into a Pandas DataFrame
    print("Load spatial data")
    df = pd.read_csv(path_to_spatial)
    if method=='stereoseq':
        # stereoseq
        # extend gemfile
        print("Expanding gemfile")
        count_numbers = df['MIDCount'].unique()
        df_keep = df[df['MIDCount'] == 1]
        for i in count_numbers[count_numbers > 1]:
            print(i)
            df_ext = df[df['MIDCount'] == i]
            df_ext = pd.concat([df_ext] * i, ignore_index=True)
            df_keep = pd.concat([df_keep, df_ext], ignore_index=True)
        df = df_keep  
        del df_keep
        del df_ext
        df['MIDCount'] = 1
        df['z'] = 0
    if method=='merfish':
        df['bin1_ID'] = df.index
        df = df.drop(columns=df.columns[[0,1, 5, 6]])
        df.columns = ['geneID', 'x', 'y', 'bin1_ID']
        df['MIDCount'] = 1
        df['x'] = df['x'] - df['x'].min()
        df['y'] = df['y'] - df['y'].min()
        df['z'] = 0
    if method=='allen-merfish':
        df['bin1_ID'] = df.index
        df = df.drop(columns=df.columns[[0,1,2,3,4,7,9,10]])
        df['MIDCount'] = 1
        df = df.rename(columns={'gene': 'geneID'})
        df['z'] = 0
    if method=='xenium':
        df = df.drop(columns=df.columns[[1, 2, 7, 8,9]])
        df.columns = ['bin1_ID','geneID', 'x', 'y', 'z']
        df['MIDCount'] = 1   
    
    if mode=='cluster':
        # Load the single nuc z-score file (output from script 01) into a Pandas DataFrame
        print("Load co-expression network for cluster " + inputvalue)
        zf = pd.read_csv(path_to_network + "Cluster" + str(inputvalue) + '.csv')
        zf.columns = ['geneID', 'mean', 'sum']
        
    if mode=='gene':
        # Load the single nuc z-score file (output from script 01) into a Pandas DataFrame
        print("Load co-expression network for gene " + inputvalue)
        zf = pd.read_csv(path_to_network + 'coexpmat_z.csv')
        zf.rename(columns={ zf.columns[0]: "features" }, inplace = True)
        zf = zf.loc[zf["features"] == inputvalue].T.tail(-1)  ## or take the column??
        zf['geneID'] = zf.index
        zf.columns = ['mean', 'geneID'] 

    # merge the zscores (zf) with the DNB data (df)
    df=df.merge(zf, how='inner', on='geneID') 
    df = df[['x', 'y', 'z', 'bin1_ID', 'MIDCount', 'geneID', 'mean']]

    full_width= int(round(df['x'].max(), 0))
    full_height= int(round(df['y'].max(), 0))
    result_df = pd.DataFrame(columns=['x', 'y', 'z','bin1_ID', 'geneID', 'MIDCount', 'block_sum'])

    for x_start in range(0, full_width, block_size):
        x_end = min(x_start + block_size, full_width)
        for y_start in range(0, full_height, block_size):
            y_end = min(y_start + block_size, full_height)

            # Extract the block DataFrame
            block_df = df[
                (df['x'] >= x_start - overlap) & (df['x'] < x_end + overlap) &
                (df['y'] >= y_start - overlap) & (df['y'] < y_end + overlap)
                ]
        
            print("Processing block at x_start:", x_start, "y_start:", y_start)
        
            # Calculate block sums
            points = block_df[['x', 'y', 'z']].values
            tree = cKDTree(points)
            block_sums = []

            # Create a tqdm progress bar
            progress_bar = tqdm(total=len(block_df), desc='Calculating Block Sums', position=0, leave=True)

            for i, (x, y, z) in enumerate(points):
                indices = tree.query_ball_point([x, y, z], r)
                block_sum = np.sum(block_df['mean'].iloc[indices])
                block_sums.append(block_sum)

                # Update the progress bar
                progress_bar.update(1)

            # Close the progress bar
            progress_bar.close()
            
    # Create a DataFrame with 'x', 'y', and 'block_sum'
    result_df = pd.DataFrame({'x': block_df['x'], 'y': block_df['y'], 'z': block_df['z'], 'bin1_ID': block_df['bin1_ID'], 'geneID': block_df['geneID'], 'MIDCount': block_df['MIDCount'], 'block_sum': block_sums})
      
    # aggregate by bin1_ID
    result_df2 = pd.DataFrame(result_df.groupby(by=["bin1_ID"])["block_sum"].sum())
    result_df2['bin1_ID'] = result_df2.index
    result_df2 = result_df2.reset_index(drop=True)
    result_df = result_df2.merge(result_df[["bin1_ID", "x", "y", "z", "geneID", "MIDCount"]], on = "bin1_ID", how = "inner")
    result_df = result_df.drop_duplicates()

    if outputimageformat=='both' or outputimageformat=='tiff':  
    # create a new image 
        print("Create tiff image")
        new_image = np.zeros((full_height+1, full_width+1, 3), dtype=np.uint8)
        max_sum = result_df['block_sum'].max()
        min_sum = result_df['block_sum'].min()*-1

        normalized_values = result_df['block_sum'].values
        x_values = result_df['x'].astype(int).values
        y_values = result_df['y'].astype(int).values

        # Positive and negative values separation
        positive_mask = normalized_values >= 0
        negative_mask = ~positive_mask
        positive_values = normalized_values[positive_mask]
        negative_values = -normalized_values[negative_mask]

        # Calculate values for green and blue channels
        new_image[y_values[positive_mask], x_values[positive_mask], 1] = (positive_values * (255 / max_sum)).astype(int)
        new_image[y_values[negative_mask], x_values[negative_mask], 2] = (negative_values * (255 / min_sum)).astype(int)

        # Save or display the image
        if mode=='cluster':
            tiff.imsave('./Results/02. Mapping/' + spatial_sample_name + '/clusters/cluster' + inputvalue + '_from_' + network_name + '_r' + str(r) + '.tif', new_image)
        if mode=='gene':
            tiff.imsave('./Results/02. Mapping/' + spatial_sample_name + '/genes/' + inputvalue + '_from_' + network_name + '_r' + str(r) + '.tif', new_image)

        if fill==True:
            # Create a mask for zero pixels
            print("Create filled image")
            zero_mask = (new_image == 0)
            avg_blue = ndimage.convolve(new_image[:, :, 0], np.ones((3, 3)) / 9, mode='constant', cval=0)
            avg_green = ndimage.convolve(new_image[:, :, 1], np.ones((3, 3)) / 9, mode='constant', cval=0)
            new_image[:, :, 0][zero_mask[:, :, 0]] = avg_blue[zero_mask[:, :, 0]]
            new_image[:, :, 1][zero_mask[:, :, 1]] = avg_green[zero_mask[:, :, 1]]

            # Save or display the image
            if mode=='cluster':
                tiff.imsave('./Results/02. Mapping/' + spatial_sample_name + '/clusters/cluster' + inputvalue + '_from_' + network_name + '_fill_r' + str(r) + '.tif', new_image)
            if mode=='gene':
                tiff.imsave('./Results/02. Mapping/' + spatial_sample_name + '/genes/' + inputvalue + '_from_' + network_name + '_fill_r' + str(r) + '.tif', new_image)
        
        if outputimageformat=='both': # also make png image
            print("Create png image")
            new_image = Image.new("RGBA", (full_width+1, full_height+1), (255, 255, 255, 255))
            normalized_values = result_df['block_sum'].values
            x_values = result_df['x'].astype(int).values
            y_values = result_df['y'].astype(int).values

            # Positive and negative values separation
            positive_mask = normalized_values >= 0
            positive_values = normalized_values[positive_mask]
            positive_values_scaled = positive_values / positive_values.max()
            transparency_values = [max(100, int(255 * intensity)) for intensity in positive_values_scaled]
            pixels = new_image.load() 
            rgb_color = (255, 0, 0)
            for x, y, transparency in zip(x_values[positive_mask], y_values[positive_mask], transparency_values):
                pixels[x, y] = rgb_color + (transparency,)

            if mode=='gene' and inputvalue in result_df['geneID'].values:
                result_df_sub = result_df[result_df['geneID'] == inputvalue]
                normalized_values = result_df_sub['block_sum'].values
                x_values = result_df_sub['x'].astype(int).values
                y_values = result_df_sub['y'].astype(int).values

                # Positive and negative values separation
                positive_mask = normalized_values >= 0
                positive_values = normalized_values[positive_mask]
                positive_values_scaled = positive_values / positive_values.max()
                transparency_values = [max(50, int(255 * intensity)) for intensity in positive_values_scaled]
                rgb_color = (0, 255, 0)
                for x, y, transparency in zip(x_values[positive_mask], y_values[positive_mask], transparency_values):
                    pixels[x, y] = rgb_color + (transparency,)
           
            if mode=='cluster':
                new_image.save('./Results/02. Images/' + spatial_sample_name + '/clusters/cluster' + inputvalue + '_from_' + network_name + '_mean_r' + str(r) + '.png')
            if mode=='gene':
                new_image.save('./Results/02. Images/' + spatial_sample_name + '/genes/' + inputvalue + '_from_' + network_name + '_mean_r' + str(r) + '.png')

        del new_image

    if outputimageformat=='png':  
            new_image = Image.new("RGBA", (full_width+1, full_height+1), (255, 255, 255, 255))
            normalized_values = result_df['block_sum'].values
            x_values = result_df['x'].astype(int).values
            y_values = result_df['y'].astype(int).values

            # Positive and negative values separation
            positive_mask = normalized_values >= 0
            positive_values = normalized_values[positive_mask]
            positive_values_scaled = positive_values / positive_values.max()
            transparency_values = [max(100, int(255 * intensity)) for intensity in positive_values_scaled]
            pixels = new_image.load() 
            rgb_color = (255, 0, 0)
            for x, y, transparency in zip(x_values[positive_mask], y_values[positive_mask], transparency_values):
                pixels[x, y] = rgb_color + (transparency,)

            if mode=='gene' and inputvalue in result_df['geneID'].values: 
                result_df_sub = result_df[result_df['geneID'] == inputvalue]
                normalized_values = result_df_sub['block_sum'].values
                x_values = result_df_sub['x'].astype(int).values
                y_values = result_df_sub['y'].astype(int).values

                # Positive and negative values separation
                positive_mask = normalized_values >= 0
                positive_values = normalized_values[positive_mask]
                positive_values_scaled = positive_values / positive_values.max()
                transparency_values = [max(50, int(255 * intensity)) for intensity in positive_values_scaled]
                rgb_color = (0, 255, 0)
                for x, y, transparency in zip(x_values[positive_mask], y_values[positive_mask], transparency_values):
                    pixels[x, y] = rgb_color + (transparency,)

            if mode=='cluster':
                new_image.save('./Results/02. Mapping/' + spatial_sample_name + '/clusters/cluster' + inputvalue + '_from_' + network_name + '_mean_r' + str(r) + '.png')
            if mode=='gene':
                new_image.save('./Results/02. Mapping/' + spatial_sample_name + '/genes/' + inputvalue + '_from_' + network_name + '_mean_r' + str(r) + '.png')
            new_image.close()

    # plot histogram
    fix, axs = plt.subplots(1, 1, figsize =(10,7), tight_layout = True)
    axs.hist(result_df['block_sum'], bins = 100)
    plt.axvline(x = 0, color = 'r')
    if mode=='cluster':
        plt.savefig('./Results/02. Mapping/' + spatial_sample_name + '/clusters/cluster' + inputvalue + '_from_' + network_name + '_mean_r' + str(r) + '_thres0_sumblocksums.pdf', format = 'pdf')
    if mode=='gene':
        plt.savefig('./Results/02. Mapping/' + spatial_sample_name + '/genes/' + inputvalue + '_from_' + network_name + '_mean_r' + str(r) + '_thres0_sumblocksums.pdf', format = 'pdf')
    plt.close()
        
    # save total counts under the mask
    ## scale based on block sum intensity of that point?? 
    result_df_sub = result_df.loc[result_df['block_sum'] > 0]
    result_df_sub['MIDCount_blocksum'] = result_df_sub['block_sum']
    res = pd.DataFrame(result_df_sub.groupby(by=["geneID"])["MIDCount"].sum())
    res2 = pd.DataFrame(result_df_sub.groupby(by=["geneID"])["MIDCount_blocksum"].sum()) ### new
    res=pd.DataFrame({'geneID': res.index,'MIDCount': res['MIDCount'], 'MIDCount_blocksum': res2['MIDCount_blocksum']}) ### new
    res['MIDCount_totpixel_fraction'] = res['MIDCount'] / int(len(result_df_sub))
    
    if mode=='cluster':
        res.to_csv('./Results/02. Mapping/' + spatial_sample_name + '/clusters/cluster' + inputvalue + '_from_' + network_name + '_mean_r' + str(r) + '_countsundermask.csv', index=False)
    if mode=='gene':
        res.to_csv('./Results/02. Mapping/' + spatial_sample_name + '/genes/' + inputvalue + '_from_' + network_name + '_mean_r' + str(r) + '_countsundermask.csv', index=False)


    # result_df_sub
    if mode=='cluster':
        result_df_sub.to_csv('./Results/02. Mapping/' + spatial_sample_name + '/clusters/cluster' + inputvalue + '_from_' + network_name + '_mean_r' + str(r) + '_result_df_sub.csv', index=False)
    if mode=='gene':
        result_df_sub.to_csv('./Results/02. Mapping/' + spatial_sample_name + '/genes/' + inputvalue + '_from_' + network_name + '_mean_r' + str(r) + '_result_df_sub.csv', index=False)



def MakeCombinedImage(spatial_sample_name, method,network_name, r, clusters, colors):
    for cluster in clusters:
        csv_file = './Results/02. Mapping/'+ spatial_sample_name + '/clusters/cluster' + str(cluster) + '_from_' + network_name + '_mean_r' + str(r) + '_result_df_sub.csv'
        bf = pd.read_csv(csv_file)
        bf = bf.drop(columns=bf.columns[[4,6]])
        bf = bf.drop_duplicates()
        
        if cluster!=clusters[0]:
            print('Adding cluster' + str(cluster))
            overlap_merged=bf.merge(bf2, how='outer', on='bin1_ID') 
            
            toreplace1 = overlap_merged.loc[overlap_merged['block_sum_x'] > overlap_merged['block_sum_y']]
            toreplace2 = overlap_merged[overlap_merged['block_sum_x'].notna() & overlap_merged['block_sum_y'].isna()]

            bf = pd.concat([toreplace1, toreplace2], axis=0)  
            bf = bf.rename(columns={'block_sum_x': 'block_sum'})
            bf = bf.rename(columns={'x_x': 'x'})
            bf = bf.rename(columns={'y_x': 'y'})
       
        # create a new image for first cluster
        if cluster==clusters[0]:        
            print("Create new image")
            full_width= int(bf['x'].max()) + 5
            full_height= int(bf['y'].max()) + 5
            new_image = Image.new("RGBA", (full_width+1, full_height+1), (255, 255, 255, 255))

        # Extract relevant columns from the DataFrame
        normalized_values = bf['block_sum'].values
        x_values = bf['x'].astype(int).values
        y_values = bf['y'].astype(int).values

        # Positive and negative values separation
        positive_mask = normalized_values >= 0
        positive_values = normalized_values[positive_mask]
        positive_values_scaled = positive_values / positive_values.max()
        transparency_values = [max(100, int(255 * intensity)) for intensity in positive_values_scaled]

        if cluster==clusters[0]: 
            pixels = new_image.load()        

        rgb_color = colors.iloc[cluster,:]
        rgb_color = tuple(rgb_color.loc[['R', 'G', 'B']])
        rgb_color = tuple(map(int, rgb_color)) 

        for x, y, transparency in zip(x_values[positive_mask], y_values[positive_mask], transparency_values):
            # Set RGB values with constant color and varying transparency
            pixels[x, y] = rgb_color + (transparency,)

        bf2 = bf.loc[:,["x", "y", "bin1_ID", "block_sum"]]
        
    new_image.save('./Results/02. Mapping/' + spatial_sample_name + '/Overlay_from_' + network_name + '_mean_r' + str(r) + '.png')
    new_image_keep_to_fill = new_image

    if method=='xenium':
        # load nuclei and cell boundaries
        csv_file = '/Users/emma/OneDrive - Karolinska Institutet/2. Postdoc KI/Other/10x/' + spatial_sample_name + '_outs/nucleus_boundaries.csv'
        nuclei = pd.read_csv(csv_file)
        csv_file = '/Users/emma/OneDrive - Karolinska Institutet/2. Postdoc KI/Other/10x/' + spatial_sample_name + '_outs/cell_boundaries.csv'
        cells = pd.read_csv(csv_file)
   
        # plot nuclei
        rgb_color = (0, 0, 0)
        for x, y in zip(nuclei['vertex_x'], nuclei['vertex_y']):
            pixels[x, y] = rgb_color
           
        # add cell boundaries    
        rgb_color = (0, 0, 255)
        for x, y in zip(cells['vertex_x'], cells['vertex_y']):
            pixels[x, y] = rgb_color

        new_image.save('./Results/02. Mapping/' + spatial_sample_name + '/Overlay_from_' + network_name + '_mean_r' + str(r) + '_withnuclei.png')         
    
    print("Create filled image")
    image_array = np.array(new_image_keep_to_fill)
    zero_mask = (image_array == 0)

    # Calculate the average of non-zero neighbors along each channel
    avg_red = ndimage.convolve(image_array[:, :, 0], np.ones((3, 3)) / 9, mode='constant', cval=0)
    avg_green = ndimage.convolve(image_array[:, :, 1], np.ones((3, 3)) / 9, mode='constant', cval=0)
    avg_blue = ndimage.convolve(image_array[:, :, 2], np.ones((3, 3)) / 9, mode='constant', cval=0)

    # Update zero pixels with calculated averages
    image_array[:, :, 0][zero_mask[:, :, 0]] = avg_red[zero_mask[:, :, 0]]
    image_array[:, :, 1][zero_mask[:, :, 1]] = avg_green[zero_mask[:, :, 1]]
    image_array[:, :, 2][zero_mask[:, :, 2]] = avg_blue[zero_mask[:, :, 2]]
    
    tiff.imsave('./Results/02. Mapping/' + spatial_sample_name + '/Overlay_from_' + network_name + '_mean_r' + str(r) + '_filled.tiff', image_array)


           

    
