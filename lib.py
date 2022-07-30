# There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

# input
# customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
# n: a positive integer, the number of checkout tills.
# output
# The function should return an integer, the total time required.

from sklearn import naive_bayes


def queue_time(customers, n):
    time = 0
    if customers == []:
        return time
    at_tills = customers[0:n]
    waiting = customers[n:len(customers)]
    while len(waiting) >= 1:
        time = time + min(at_tills)
        at_tills = list(map(lambda x: x - min(at_tills), at_tills))

        for till in at_tills:
            if till == 0 and len(waiting) != 0:
                at_tills.insert(at_tills.index(0), waiting[0])
                waiting.pop(0)
                at_tills.remove(0)

    time = time + max(at_tills)
    return time


if __name__ == "__main__":
    print(queue_time([15, 25, 15, 15], 3))
