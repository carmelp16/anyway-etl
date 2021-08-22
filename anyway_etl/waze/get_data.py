from anyway_etl.waze.utils import DataRetriever, WazeDataFlowsHandler


def get_waze_data() -> dict:
    data_retriever, dataflows_handler = DataRetriever(), WazeDataFlowsHandler()

    waze_data = data_retriever.get_data()

    dataflows = dataflows_handler.get_dataflows(waze_data)

    for dataflow in dataflows:
        dataflow.process()


if __name__ == "__main__":
    get_waze_data()
