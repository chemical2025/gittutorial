import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

cost_of_apple = 1000
cost_of_banana = 2000
def calculate_total_cost(apple_count, banana_count):
    total_cost = (cost_of_apple * apple_count) + (cost_of_banana * banana_count)
    logger.info(f"Total cost calculated: {total_cost}")
    return total_cost
def main():
    apple_count = 5
    banana_count = 3
    total_cost = calculate_total_cost(apple_count, banana_count)
    print(f"Total cost for {apple_count} apples and {banana_count} bananas is: {total_cost}")

if __name__ == "__main__":
    main()