from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent

#from backend import run_travel_agent

res = run_travel_agent("Plan a 3-day trip to Paris")

print("=== ANSWER ===")
print(res["answer"])

print("\n=== ITINERARY ===")
print(res["itinerary"])