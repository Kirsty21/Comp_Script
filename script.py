def compare_excel_files(file_paths, output_file):
    # Read all Excel files into pandas DataFrames
    data_frames = [pd.read_excel(file) for file in file_paths]
    
    # Check if all files have the same structure (columns)
    columns = data_frames[0].columns
    for df in data_frames[1:]:
        if not df.columns.equals(columns):
            print("Warning: Columns are not the same across all files")
            return
    
    # Initialize a list to collect the differences
    differences = []

    # Compare each pair of files (assuming they have the same structure)
    base_df = data_frames[0]
    
    for i, df in enumerate(data_frames[1:], 1):
        # Find rows that are in base_df but not in df
        diff1 = pd.concat([base_df, df]).drop_duplicates(keep=False)
        diff1['Source File'] = file_paths[0]  # Mark source
        diff1['Comparison With'] = file_paths[i]
        differences.append(diff1)

    # Concatenate all differences
    final_diff = pd.concat(differences, ignore_index=True)
    
    # Write the differences to a new Excel file
    final_diff.to_excel(output_file, index=False)

    print(f"Differences saved to {output_file}")

# Example usage
file_paths = ["file1.xlsx", "file2.xlsx", "file3.xlsx"]  # Replace with actual file paths
output_file = "differences_output.xlsx"  # Output file name
compare_excel_files(file_paths, output_file)
