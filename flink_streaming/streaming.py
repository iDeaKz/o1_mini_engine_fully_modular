from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.functions import MapFunction, ProcessFunction, Collector

class ParseEvent(MapFunction):
    def map(self, value: str):
        event_type, count = value.split(",")
        return event_type, int(count)

class SumCounts(ProcessFunction):
    def __init__(self):
        self.counts = {}

    def process_element(self, value, ctx, out: Collector):
        event_type, count = value
        self.counts[event_type] = self.counts.get(event_type, 0) + count
        out.collect((event_type, self.counts[event_type]))

def main():
    env = StreamExecutionEnvironment.get_execution_environment()
    events = env.from_collection(["click,1", "view,2", "click,3", "purchase,1", "view,1", "click,2"])
    parsed_events = events.map(ParseEvent())
    summed_events = parsed_events.process(SumCounts())
    summed_events.print()
    env.execute("Streaming Analytics")

if __name__ == "__main__":
    main()
