import os
from osdata.data_loaders.base import DataLoader, extract_dir_and_basename_from_url
from osdata.ai import AiAssist
from osdata.analytics import AnalyticsService, Events


class Dataset:
    def __init__(self, alias: str) -> None:
        self.__dl = DataLoader()
        self.__ai_assist = AiAssist()
        self.__analytics = AnalyticsService()
        self.df = None
        self.alias = alias
        self.__load(alias)

    def __load(self, alias: str):
        ds_path, loader = self.__dl.find_by_alias(alias)
        tup = extract_dir_and_basename_from_url(ds_path)
        if ds_path:
            dir, filename = tup[0], tup[1]
            # Get local file path
            base_path = '.osyris/datasets/{dir}/{filename}'.format(
                dir=dir, filename=filename)
            root = os.path.expanduser('~')
            local_path = os.path.join(root, base_path)
            # If it does not exist download it first
            if not os.path.exists(local_path):
                print('Downloading dataset to:', local_path)
                local_path = self.__dl.download_file(
                    ds_path, local_path)
                # Update analytics
                self.__analytics.track(Events.DATASET_DOWNLOADED.value, {
                                       'dataset_name': self.alias})
            # Load the file and return the dataframe
            return self.__run_loader(local_path, loader)

    def ai(self, prompt: str):
        globals_context = globals()
        # Get the code from the user query
        code = self.__ai_assist.get_code_str(
            {"analysis_question": prompt, "language": "python", **self.__dl.metadata})
        try:
            # Run the code
            exec(code, globals_context, {'df': self.df})
            # Update analytics
            self.__analytics.track(Events.DATASET_AI_QUERIED.value, {
                                   'dataset_name': self.alias, 'query': prompt})
            # Store the dataframe
            df = locals['df']
            return df
        except Exception as e:
            print(f"Error executing code: {e}")

    # def clean(self):
    #     pass

    # def normalize(self, **kwargs):
    #     pass

    def __run_loader(self, file_path, loader):
        globals_context = globals()
        context = {'file_path': file_path}
        code = loader.replace("\\n", "\n")
        try:
            print('Loading dataset')
            # Run the loading code
            exec(code, globals_context, context)
            df = context['df']
            # Store the dataframe
            self.df = df
            # Update analytics
            self.__analytics.track(Events.DATASET_LOADED.value, {
                'dataset_name': self.alias})
            return df
        except Exception as e:
            print(f"Error executing code: {e}")
