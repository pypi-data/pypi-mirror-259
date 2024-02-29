#import bundling_score.bundling_score as bs
import sys
import os
import pandas as pd
from skimage import io
import bundling_score.bundling_score as bs


def main():
    print(os.getcwd())
    test = False
    while not test:
        print("Enter source folder")
        source_dir = input()
        if not os.path.isdir(source_dir):
            print("Folder does not exist, retry")
        else:
            test = True

    test = False
    while not test:
        print("Window size is 20px, do you want to change it? (y/n)")
        if input() in ['y', 'yes', 'YES', 'Y']:
            print("Enter window size (px)")
            try:
                smax = int(input())
                test = True
            except ValueError:
                print("Window size has to be an integer.")
        else:
            smax = 20
            test = True

    ic = io.MultiImage(os.path.join(source_dir, '*.tif'), dtype=float)

    print(f"{len(ic)} files detected.")

    # Bundling scores will be stored in a DataFrame
    df = pd.DataFrame()

    for i, timelapse in enumerate(ic):
        # Get only the name of the file
        name = ic.files[i][len(source_dir):-4]
        # Load ROI and crop
        timelapse = timelapse.astype(float)

        scores = []

        for j in range(timelapse.shape[0]):
            scores.append(bs.compute_score(timelapse[j, ...], smax=20))

        # Header is the name of the tif file
        series = pd.Series(scores, name=name)
        # Add to the main dataframe
        df = pd.concat((df, series), axis=1)

    save_path = os.path.join(source_dir, 'bundling_scores.csv')
    df.to_csv(save_path)

    print('Success! Data are stored in ' + save_path)
    print('Remember to multiply by the square of the resolution!')


if __name__ == "__main__":
    main()
