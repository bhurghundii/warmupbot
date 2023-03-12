class OutputData:
    def __init__(self, df):
        self.df = df
        self.unique_genres = df["Genre"].unique()

    def output_data(self):
        for genre in self.unique_genres:
            genre_data = self.df.loc[self.df['Genre'] == genre]
            self._output_genre_tasks(genre, genre_data)

    def _output_genre_tasks(self, genre, genre_data):
        print(f"## Task for {genre}")
        for value in (genre_data.sample(1).values):
            self._output_task(value)

    def _output_task(self, task_data):
        task_name = task_data[0]
        task_source = str(task_data[1])

        print(f"- [ ] {task_name}")
        print(f"Source: {task_source}")
        print(f"\n \n")