import os
import datetime
from ..helpers import helpfunctions as _hf
from ..modules import drawing_functions as _df
from ..modules import colorscale as _cs
from ..config import analysis_types_to_execute as analysis_types_to_execute

class Pipeline:
    """
    Class for executing different analyses on KEGG pathways with various data inputs.

    Parameters:
    - input_file_path (str or list): Path to the input file or a list of input files.
    - sheet_name_paths (str): Sheet name containing pathway information.
    - sheet_name_genes (str): Sheet name containing gene information.
    - genes_column (str): Column name for genes in in the sheet_name_genes.
    - log2fc_column (str): Column name for log2 fold change in in the sheet_name_genes.
    - analysis_type (int): Type of analysis to be performed.
    - input_label (str or list): Label or list of labels for the input files.
    - methylation_path (str): Path to the methylation file.
    - methylation_pvalue (str): Column name for p-value in methylation file.
    - methylation_genes (str): Column name for genes in methylation file.
    - methylation_pvalue_thresh (float): Threshold for methylation p-value.
    - miRNA_path (str): Path to the miRNA file.
    - miRNA_pvalue (str): Column name for p-value in miRNA file.
    - miRNA_genes (str): Column name for genes in miRNA file.
    - miRNA_pvalue_thresh (float): Threshold for miRNA p-value.
    - folder_extension (str): Extension for the output folder.

    - count_threshold (int): Threshold for gene count.
    - benjamini_threshold (float): Threshold for Benjamini correction.
    - save_to_eps (bool): Flag to save output to EPS format.

    Methods:
    - select_analysis(): Selects and executes the specified analysis type.

    Analysis Types:
    1. Single input (Gene IDs)
    2. Single input (Transcript IDs)
    3. Multiple inputs
    4. Single input with Methylation
    5. Single input with miRNA
    6. Single input with Methylation and miRNA
    7. Single input (Bulk mapping)
    """
    def __init__(self, input_file_path, sheet_name_paths, sheet_name_genes, analysis_type=None, input_label=None,
                methylation_path=None, methylation_pvalue=None, methylation_genes=None, methylation_pvalue_thresh=0.05,
                miRNA_path=None, miRNA_pvalue=None, miRNA_genes=None, miRNA_pvalue_thresh=0.05,
                folder_extension=None, genes_column='gene_symbol', log2fc_column='logFC', count_threshold=2, benjamini_threshold=None ,save_to_eps=False):

        self.input_file_path = input_file_path
        self.sheet_name_paths = sheet_name_paths
        self.sheet_name_genes = sheet_name_genes
        self.folder_extension = folder_extension
        self.genes_column = genes_column
        self.log2fc_column = log2fc_column
        self.analysis_type = analysis_type
        self.count_threshold = count_threshold
        self.input_label = input_label
        self.methylation_path = methylation_path
        self.methylation_pvalue = methylation_pvalue
        self.methylation_genes = methylation_genes
        self.methylation_pvalue_thresh = methylation_pvalue_thresh
        self.miRNA_path = miRNA_path
        self.miRNA_pvalue = miRNA_pvalue
        self.miRNA_genes = miRNA_genes
        self.miRNA_pvalue_thresh = miRNA_pvalue_thresh

        self.benjamini_threshold = benjamini_threshold
        self.save_to_eps = save_to_eps

        self.select_analysis()

    def select_analysis(self):
        """
        Selects and executes the specified analysis type based on the provided parameters.

        Returns:
        None
        """
        valid_analysis_types = set([1, 2, 3, 4, 5, 6, 7])
        
        if self.analysis_type in valid_analysis_types:
            if self.analysis_type == 1:
                self.single_input_genes()
            elif self.analysis_type == 2:
                self.single_input_transcripts()
            elif self.analysis_type == 3:
                self.multiple_inputs()
            elif self.analysis_type == 4:
                self.single_input_with_methylation()
            elif self.analysis_type == 5:
                self.single_input_with_miRNA()
            elif self.analysis_type == 6:
                self.single_input_with_methylation_and_miRNA()
            elif self.analysis_type == 7:
                self.single_input_genes_bulk_mapping()
        elif self.analysis_type is None:
            print('Initialized class. Have to run analysis in expert mode.\nValid choices are:')
            for value in analysis_types_to_execute.values():
                print(f'{value}')
            pass
        else:
            raise ValueError(f"Invalid analysis type: {self.analysis_type}. Please provide a value between 1 and 7.")

    def find_file_folder(self):
        """
        Find the folder containing the input file(s) and set the current working directory to that location.

        Returns:
        str: The path to the folder containing the input file(s).

        Raises:
        FileNotFoundError: If the specified file or the first file in the list (for multiple files) does not exist.
        """
        if isinstance(self.input_file_path, list):
            if os.path.exists(self.input_file_path[0]):
                folder_path = os.path.dirname(self.input_file_path[0])
                os.chdir(folder_path)
                return folder_path
            else:
                raise FileNotFoundError(f"The file '{self.input_file_path[0]}' does not exist.")
        
        else:
            if os.path.exists(self.input_file_path):
                folder_path = os.path.dirname(self.input_file_path)
                os.chdir(folder_path)
                return folder_path
            else:
                raise FileNotFoundError(f"The file '{self.input_file_path}' does not exist.")
        
    def make_output_folder(self , folder_path , analysis_extension):
        """
        Create a unique output folder based on the current date, analysis extension, and an optional folder extension.

        Args:
        folder_path (str): The path to the folder where the output folder will be created.
        analysis_extension (str): A string representing the type of analysis being performed.

        Returns:
        str: The path to the created output folder.

        Notes:
        - The output folder is named in the format: "draw_KEGG_<current_date>_<analysis_extension>_<folder_extension>"
        - The folder_extension is optional and can be set during the class initialization.
        """
        today = datetime.date.today().strftime("%Y-%m-%d")
        folder_today = f"draw_KEGG_{today}_{analysis_extension}"
        create_folder = os.path.join(folder_path, folder_today)
        print(create_folder)
        output_folder = _hf.create_output_folder(create_folder, self.folder_extension)
        return output_folder

    def single_input_genes(self):
        """
        Perform the Single Input Analysis for Gene IDs.

        Raises:
        TypeError: If the input_file_path is a list, as this analysis expects a single input file.

        Prints:
        - Execution message.
        - Output folder path.
        - Parsing and collecting pathway information messages.
        - Completion message.

        Notes:
        - Calls helper functions to filter KEGG pathways for genes, parse the input file, and draw KEGG pathways.
        - The output files are located in the created output folder.
        """   
        if isinstance(self.input_file_path , list):
            raise TypeError('Please provide a single input to perform \'Single input analysis (Genes)')

        print("Executing analysis: Single input (Gene IDs)...")
        folder_of_input = self.find_file_folder()

        analysis_extension = 'genes'
        output_folder = self.make_output_folder(folder_of_input , analysis_extension)
        print(f'Output folder is {output_folder}')
        parsed_out = _hf.filter_kegg_pathways_genes(filepath=self.input_file_path,
                                                    sheet_name_paths=self.sheet_name_paths,
                                                    sheet_name_genes=self.sheet_name_genes,
                                                    genes_column= self.genes_column,
                                                    log2fc_column=self.log2fc_column,
                                                    count_threshold = self.count_threshold , benjamini_threshold=self.benjamini_threshold)
        print('Finished parsing input file')
        pathway_info = _hf.collect_pathway_info(parsed_output=parsed_out)
        print('Finished collecting pathway info')
        os.chdir(output_folder)
        _df.draw_KEGG_pathways_genes(parsed_output=parsed_out , info=pathway_info , save_to_eps=self.save_to_eps)
        print(f'Finished analysis! \nOutput files are located in {output_folder}')

    def single_input_transcripts(self):
        """
        Perform the Single Input Analysis for Transcript IDs.

        Raises:
        TypeError: If the input_file_path is a list, as this analysis expects a single input file.

        Prints:
        - Execution message.
        - Output folder path.
        - Parsing and collecting pathway information messages.
        - Completion message.

        Notes:
        - Calls helper functions to filter KEGG pathways for genes, parse the input file, and draw KEGG pathways for transcripts.
        - The output files are located in the created output folder.
        """
        if isinstance(self.input_file_path , list):
            raise TypeError('Please provide a single input to perform \'Single input analysis (Transcripts)')
        
        print("Executing analysis: Single input (Transcript IDs)...")
        folder_of_input = self.find_file_folder()
        analysis_extension = 'transcripts'
        output_folder = self.make_output_folder(folder_of_input , analysis_extension)
        print(f'Output folder is {output_folder}')
        
        parsed_out = _hf.filter_kegg_pathways_genes(filepath=self.input_file_path,
                                                    sheet_name_paths=self.sheet_name_paths,
                                                    sheet_name_genes=self.sheet_name_genes,
                                                    genes_column=self.genes_column,
                                                    log2fc_column=self.log2fc_column,
                                                    count_threshold = self.count_threshold , benjamini_threshold=self.benjamini_threshold)
        print('Finished parsing input file')
        pathway_info = _hf.collect_pathway_info(parsed_output=parsed_out)
        print('Finished collecting pathway info')
        os.chdir(output_folder)
        _df.draw_KEGG_pathways_transcripts(parsed_output=parsed_out , info=pathway_info , save_to_eps=self.save_to_eps)

    def multiple_inputs(self):
        """
        Perform the Multiple Inputs Analysis.

        Raises:
        TypeError: If the input_file_path is not a list, if the input_label is not a list,
                or if the number of input files does not match the number of labels.

        Prints:
        - Execution message.
        - Output folder path.
        - Information about the number of inputs to be mapped.
        - Parsing and collecting pathway information messages.
        - Completion message.

        Notes:
        - Calls helper functions to filter KEGG pathways for genes, parse input files for multiple interventions,
        and draw KEGG pathways for genes with multiple interventions.
        - The output files are located in the created output folder.
        """
        if not isinstance(self.input_file_path , list):
            raise TypeError('Please provide a list of inputs to perform \'Multiple inputs analysis')
        elif not isinstance(self.input_label , list):
            raise TypeError('Please provide a list with a label for each input file.')
        elif isinstance(self.input_label , list) and isinstance(self.input_file_path , list) and (len(self.input_file_path) != len(self.input_label)):
            raise TypeError('Please make sure that every input file has a corresponding label.')
        print("Executing analysis : Multiple inputs...")
        
        
        how_many =  len(self.input_label)
        analysis_extension = f'{how_many}_inputs'
        
        folder_of_input = self.find_file_folder()
        output_folder = self.make_output_folder(folder_of_input , analysis_extension)
        print(f'Output folder is {output_folder}')
        if how_many > 1:
            print(f"You want to map {how_many} inputs in total.")
        else:
            raise TypeError("Please provide more than one input files to perform this analysis")

        parsed_out_list = []
        file_counter = 1

        for (file, inter_name), file_counter in zip(zip(self.input_file_path, self.input_label), range(1, len(self.input_file_path) + 1)):
            print(f"File Counter: {file_counter}, File: {file}, with name {inter_name}")
            parsed_out_counter = 'parsed_out_' + str(file_counter)
            globals()[parsed_out_counter] =  _hf.filter_kegg_pathways_genes(filepath=file,
                                                                            sheet_name_paths=self.sheet_name_paths,
                                                                            sheet_name_genes=self.sheet_name_genes,
                                                                            genes_column=self.genes_column,
                                                                            log2fc_column=self.log2fc_column,
                                                                            count_threshold = self.count_threshold , benjamini_threshold=self.benjamini_threshold,
                                                                            number_interventions=file_counter , name_interventions=inter_name)

            parsed_out_list.append(globals()[parsed_out_counter])

            file_counter += 1

        os.chdir(output_folder)
        _df.draw_KEGG_pathways_genes_multiple_interventions(parsed_out_list=parsed_out_list , intervention_names=self.input_label , colors_list=_cs.colors_list , save_to_eps=self.save_to_eps)
        print(f'Finished analysis! \nOutput files are located in {output_folder}')

    def single_input_with_methylation(self):
        """
        Perform Single Input Analysis with Methylation.

        Raises:
        TypeError: If the input_file_path is a list.

        ValueError: If the methylation file path is not provided or is invalid, or if there are no genes with a methylation profile.

        Prints:
        - Execution message.
        - Output folder path.
        - Parsing and collecting pathway information messages.
        - Completion message.

        Notes:
        - Calls helper functions to load and evaluate methylation metadata, filter KEGG pathways for genes with methylation,
        and draw KEGG pathways for genes with methylation.
        - The output files are located in the created output folder.
        """
        if isinstance(self.input_file_path , list):
            raise TypeError('Please provide a single input to perform \'Single input analysis w Methylation')
        
        print("Executing analysis : Single input w Methylation...")

        folder_of_input = self.find_file_folder()
        analysis_extension = 'methylation'
        output_folder = self.make_output_folder(folder_of_input , analysis_extension)
        print(f'Output folder is {output_folder}')
        
        if self.methylation_path is not None or isinstance(self.methylation_path, (str , os.PathLike)):
            try:
                methylation_df = _hf.load_metadata(self.methylation_path)
            except ValueError:
                raise ValueError(f'Please provide a proper methylation file path')
            
        _hf.evaluate_metadata(methylation_df , self.methylation_pvalue , self.methylation_genes)

        if self.methylation_pvalue_thresh is None or not isinstance(self.methylation_pvalue_thresh, (int, float)) or self.methylation_pvalue is None:
            genes_from_MM = methylation_df[self.methylation_genes].unique().tolist()
        else:
            if self.methylation_pvalue is not None and self.methylation_pvalue not in methylation_df.columns:
                raise KeyError(f'Column {self.methylation_pvalue} not found in the methylation dataframe.')
            
            try:
                genes_from_MM = methylation_df.loc[methylation_df[self.methylation_pvalue] < self.methylation_pvalue_thresh][self.methylation_genes].unique().tolist()
            except ValueError:
                raise ValueError(f'Invalid value provided for pvalue_thresh. It should be a number.')

        if len(genes_from_MM) == 0:
            raise ValueError('There are no genes with a methylation profile')
        
        methylation_options = ['Differentially methylated' , 'Not differentially methylated']
        color_to_methylation = { meth : color for (meth , color) in zip(methylation_options , _cs.colors_list)}

        parsed_out = _hf.filter_kegg_pathways_genes(filepath=self.input_file_path,
                                                    sheet_name_paths=self.sheet_name_paths,
                                                    sheet_name_genes=self.sheet_name_genes,
                                                    genes_column=self.genes_column,
                                                    log2fc_column=self.log2fc_column,
                                                    count_threshold = self.count_threshold,  benjamini_threshold=self.benjamini_threshold)
        print('Finished parsing input file')
        pathway_info = _hf.collect_pathway_info(parsed_output=parsed_out)
        print('Finished collecting pathway info')
        os.chdir(output_folder)
        _df.draw_KEGG_pathways_genes_with_methylation(parsed_output=parsed_out , info=pathway_info , genes_from_MM=genes_from_MM , color_legend=color_to_methylation , save_to_eps=self.save_to_eps)
        print(f'Finished analysis! \nOutput files are located in {output_folder}')

    def single_input_with_miRNA(self):
        """
        Perform Single Input Analysis with miRNA.

        Raises:
        TypeError: If the input_file_path is a list.

        ValueError: If the miRNA file path is not provided or is invalid, or if there are no genes with a miRNA profile.

        Prints:
        - Execution message.
        - Output folder path.
        - Parsing and collecting pathway information messages.
        - Completion message.

        Notes:
        - Calls helper functions to load and evaluate miRNA metadata, filter KEGG pathways for genes with miRNA,
        and draw KEGG pathways for genes with miRNA.
        - The output files are located in the created output folder.
        """
        if isinstance(self.input_file_path , list):
            raise TypeError('Please provide a single input to perform \'Single input analysis w miRNA')
        
        print("Executing analysis : Single input w miRNA...")

        folder_of_input = self.find_file_folder()    
        analysis_extension = 'miRNA'
        output_folder = self.make_output_folder(folder_of_input , analysis_extension)
        print(f'Output folder is {output_folder}')

        if self.miRNA_path is not None or isinstance(self.miRNA_path, (str , os.PathLike)):
            try:
                miRNA_df = _hf.load_metadata(self.miRNA_path)
            except ValueError:
                raise ValueError(f'Please provide a proper miRNA file path')

        _hf.evaluate_metadata(miRNA_df , self.miRNA_pvalue , self.miRNA_genes)

        if self.miRNA_pvalue_thresh is None or not isinstance(self.miRNA_pvalue_thresh, (int, float)) or self.miRNA_pvalue is None:
            genes_from_miRNA = miRNA_df[self.miRNA_genes].unique().tolist()
        else:
            if self.miRNA_pvalue is not None and self.miRNA_pvalue not in miRNA_df.columns:
                raise KeyError(f'Column {self.miRNA_pvalue} not found in the miRNA dataframe.')
            
            try:
                genes_from_miRNA = miRNA_df.loc[miRNA_df[self.miRNA_pvalue] < self.miRNA_pvalue_thresh][self.miRNA_genes].unique().tolist()
            except ValueError:
                raise ValueError(f'Invalid value provided for pvalue_thresh. It should be a number.')

        if len(genes_from_miRNA) == 0:
            raise ValueError('There are no genes with a miRNA profile')

        miRNA_options = ['miRNA detected' , 'miRNA not detected']
        color_to_miRNA = {miRNA : color for (miRNA , color) in zip(miRNA_options , _cs.colors_list)}

        parsed_out = _hf.filter_kegg_pathways_genes(filepath=self.input_file_path,
                                                    sheet_name_paths=self.sheet_name_paths,
                                                    sheet_name_genes=self.sheet_name_genes,
                                                    genes_column=self.genes_column,
                                                    log2fc_column=self.log2fc_column,
                                                    count_threshold = self.count_threshold , benjamini_threshold=self.benjamini_threshold)
        print('Finished parsing input file')
        pathway_info = _hf.collect_pathway_info(parsed_output=parsed_out)
        print('Finished collecting pathway info')
        os.chdir(output_folder)
        _df.draw_KEGG_pathways_genes_with_miRNA(parsed_output=parsed_out , info=pathway_info , genes_from_miRNA=genes_from_miRNA , color_legend=color_to_miRNA , save_to_eps=self.save_to_eps)
        print(f'Finished analysis! \nOutput files are located in {output_folder}')

    def single_input_with_methylation_and_miRNA(self):
        """
        Perform a single input analysis with Methylation and miRNA data.

        Raises:
            TypeError: If input_file_path is a list.
            ValueError: If there are issues with loading methylation or miRNA metadata.
                        If invalid values are provided for pvalue_thresh.
            KeyError: If a specified column is not found in the metadata dataframe.

        Prints:
            Execution message.
            Output folder location.

        Returns:
            None. Results are saved in the output folder.
        """
        if isinstance(self.input_file_path , list):
            raise TypeError('Please provide a single input to perform \'Single input analysis w Methylation & miRNA')
        
        print("Executing analysis : Single input w Methylation & miRNA...")

        folder_of_input = self.find_file_folder()    
        analysis_extension = 'methylation_and_miRNA'
        output_folder = self.make_output_folder(folder_of_input , analysis_extension)
        print(f'Output folder is {output_folder}')

        if self.methylation_path is not None or isinstance(self.methylation_path, (str , os.PathLike)):
            try:
                methylation_df = _hf.load_metadata(self.methylation_path)
            except ValueError:
                raise ValueError(f'Please provide a proper methylation file path')


        _hf.evaluate_metadata(methylation_df , self.methylation_pvalue , self.methylation_genes)

        if self.methylation_pvalue_thresh is None or not isinstance(self.methylation_pvalue_thresh, (int, float)) or self.methylation_pvalue is None:
            genes_from_MM = methylation_df[self.methylation_genes].unique().tolist()
        else:
            if self.methylation_pvalue is not None and self.methylation_pvalue not in methylation_df.columns:
                raise KeyError(f'Column {self.methylation_pvalue} not found in the methylation dataframe.')
            
            try:
                genes_from_MM = methylation_df.loc[methylation_df[self.methylation_pvalue] < self.methylation_pvalue_thresh][self.methylation_genes].unique().tolist()
            except ValueError:
                raise ValueError(f'Invalid value provided for pvalue_thresh. It should be a number.')

        if len(genes_from_MM) == 0:
            raise ValueError('There are no genes with a methylation profile')


        if self.miRNA_path is not None or isinstance(self.miRNA_path, (str , os.PathLike)):
            try:
                miRNA_df = _hf.load_metadata(self.miRNA_path)
            except ValueError:
                raise ValueError(f'Please provide a proper miRNA file path')
            

        _hf.evaluate_metadata(miRNA_df , self.miRNA_pvalue , self.miRNA_genes)

        if self.miRNA_pvalue_thresh is None or not isinstance(self.miRNA_pvalue_thresh, (int, float)) or self.miRNA_pvalue is None:
            genes_from_miRNA = miRNA_df[self.miRNA_genes].unique().tolist()
        else:
            if self.miRNA_pvalue is not None and self.miRNA_pvalue not in miRNA_df.columns:
                raise KeyError(f'Column {self.miRNA_pvalue} not found in the miRNA dataframe.')
            
            try:
                genes_from_miRNA = miRNA_df.loc[miRNA_df[self.miRNA_pvalue] < self.miRNA_pvalue_thresh][self.miRNA_genes].unique().tolist()
            except ValueError:
                raise ValueError(f'Invalid value provided for pvalue_thresh. It should be a number.')

        if len(genes_from_miRNA) == 0:
            raise ValueError('There are no genes with a miRNA profile')
        

        methylation_w_miRNA_options = ['Differentially methylated and miRNA detected', 'Not differentially methylated and miRNA detected',
                                       'Differentially methylated and not miRNA detected' , 'Not differentially methylated and not miRNA detected']
        color_to_methylation_w_miRNA = { meth_miRNA : color for (meth_miRNA , color) in zip(methylation_w_miRNA_options , _cs.colors_list)}

        parsed_out = _hf.filter_kegg_pathways_genes(filepath=self.input_file_path,
                                                    sheet_name_paths=self.sheet_name_paths,
                                                    sheet_name_genes=self.sheet_name_genes,
                                                    genes_column=self.genes_column,
                                                    log2fc_column=self.log2fc_column,
                                                    count_threshold = self.count_threshold , benjamini_threshold=self.benjamini_threshold)
        print('Finished parsing input file')
        pathway_info = _hf.collect_pathway_info(parsed_output=parsed_out)
        print('Finished collecting pathway info')
        os.chdir(output_folder)
        _df.draw_KEGG_pathways_genes_with_methylation_and_miRNA(parsed_output=parsed_out , info=pathway_info ,
                                                                genes_from_MM=genes_from_MM , genes_from_miRNA=genes_from_miRNA,
                                                                color_legend=color_to_methylation_w_miRNA , save_to_eps=self.save_to_eps)
        print(f'Finished analysis! \nOutput files are located in {output_folder}')

    def single_input_genes_bulk_mapping(self):
        """
        Perform a single input analysis with bulk mapping for genes.

        Raises:
            TypeError: If input_file_path is a list.

        Prints:
            Execution message.
            Output folder location.

        Returns:
            None. Results are saved in the output folder.
        """
        if isinstance(self.input_file_path , list):
            raise TypeError('Please provide a single input to perform \'Single input (Bulk mapping)')

        if self.benjamini_threshold is not None or self.count_threshold is not None:
            raise TypeError('\'Single input (Bulk mapping)\' analysis does not accept \'benjamini_threshold\' or \'count_threshold\' values. Set to None')

        print("Executing analysis : Single input (Bulk mapping)...")

        folder_of_input = self.find_file_folder()    
        analysis_extension = 'bulk'
        output_folder = self.make_output_folder(folder_of_input , analysis_extension)
        print(f'Output folder is {output_folder}')
        parsed_out = _hf.parse_bulk_kegg_pathway_file(filepath=self.input_file_path,
                                                    sheet_name_paths=self.sheet_name_paths,
                                                    sheet_name_genes=self.sheet_name_genes,
                                                    genes_column=self.genes_column, log2fc_column=self.log2fc_column)
        print('Finished parsing input file')
        pathway_info = _hf.collect_pathway_info(parsed_output=parsed_out)
        print('Finished collecting pathway info')
        os.chdir(output_folder)
        _df.draw_KEGG_pathways_genes(parsed_output=parsed_out , info=pathway_info , save_to_eps=self.save_to_eps)
        print(f'Finished analysis! \nOutput files are located in {output_folder}')