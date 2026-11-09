import src.transport as transport
import json, random, asyncio
from watchfiles import watch, Change

memory_holder: list[object] = []
slots: object | None = None

INT_TO_STRING_SINGLE = {
    1: "one", 
    2: "two", 
    3: "three", 
    4: "four", 
    5: "five", 
    6: "six", 
    7: "seven", 
    8: "eight", 
    9: "nine",
    "1": 1, 
    "2": 2, 
    "3": 3, 
    "4": 4, 
    "5": 5, 
    "6": 6, 
    "7": 7, 
    "8": 8, 
    "9": 9,
}

INT_TO_STRING_SINGLE_EDGE = {
    11: "eleven", 
    12: "twelve", 
    13: "thirteen",
    "11": 11, 
    "12": 12, 
    "13": 13,
}

INT_TO_STRING_DOUBLE = {
    10: "ten", 
    20: "twenty", 
    30: "thirty", 
    40: "forty", 
    50: "fifty", 
    60: "sixty", 
    70: "seventy", 
    80: "eighty", 
    90: "ninety", 
    100: "one hundred",
    "10": 10, 
    "20": 20, 
    "30": 30, 
    "40": 40, 
    "50": 50, 
    "60": 60, 
    "70": 70, 
    "80": 80, 
    "90": 90, 
    "100": 100
}

INT_TO_STRING_SCALE = {
    1: "ones", 
    2: "tens", 
    3: "hundred", 
    4: "thousand", 
    5: "ten thousands", 
    6: "hundred thousand", 
    7: "million", 
    8: "ten million", 
    9: "hundred million", 
    10: "billion",
}

async def continue_transport(memory: dict[str, any]) -> bool:

    transport.middleware.memory_to_store = memory

    return True
    
async def filter(change: Change, path: str) -> bool:

    if (change.modified):
        print("Neuron modified.")

    if (change.modified.bit_length > 5):
        print("Neuron potentially freed up or used.")

    return True

if (len(memory_holder) == 100):

    print(f"Loaded {len(slots['slot_status'])} slots. Starting allocation...\n")
    
    try:
        with open('Slots.json', 'r', encoding='utf-8') as file:
            
            Slots = json.load(file)
            print("Slots activated:", slots)

    except FileNotFoundError:
        print("Error: The file 'Slots.json' could not be found.")
        print("Slotting is not available, resorting to immediate memory storage")
        # Might need a dynamic short term memory creation on the fly
        raise FileNotFoundError

    except json.JSONDecodeError:
        print("Error: The file contains invalid JSON syntax.")
        print("Short term memoryed a dynamic JSON recreation logic")
        raise json.JSONDecodeError


    for memory in memory_holder:

        memory_operation_iterate = 0 
        parse_memory = json.loads(memory) 
        
        slot_status = slots["slot_status"]

        slot_activated = False
        slot_id = None

        while (slot_activated != True):

            random_available_slot = random.randint(1, 5000)

            memory_operation_iterate += 1

            if memory_operation_iterate == 20:
                
                print(f"Failsafe triggered for memory item {memory_holder.index(memory)}.")
                memory_operation_iterate = 0
                break

            if (slot_status[random_available_slot] == "Active"):

                random_available_slot = random.randint(1, 5001)
                continue

            else:

                if (len(str(random_available_slot)) in INT_TO_STRING_SCALE.keys()):

                    int_length = len(str(random_available_slot))

                    if (int_length == 3):

                        int_string = str(random_available_slot)
                        str_nums = []

                        for str_digit in int_string:

                            str_nums.append(INT_TO_STRING_SINGLE[str_digit])

                            if len(str_nums) == 1:
                                str_nums.append(INT_TO_STRING_SCALE[3])

                        str_nums[2] = INT_TO_STRING_DOUBLE[int(str_nums[2])] + "0"

                        slot_id = int("".join(str_nums))

                    if (int_length == 4):

                        int_string = str(random_available_slot)
                        str_nums = []

                        for number in int_string:

                            str_nums.append(INT_TO_STRING_SINGLE[int(number)])

                            if len(str_nums) == 1:
                                str_nums.append(INT_TO_STRING_SCALE[4])

                            if len(str_nums) == 3:
                                str_nums.append(INT_TO_STRING_SCALE[3])

                            if len(str_nums) == 4:
                                str_nums.append(INT_TO_STRING_DOUBLE[int(str_nums[2])] + "0")

                        slot_id = int("".join(str_nums))

                    if (int_length > 4):
                        print("Cannot keep up with the slot at the moment, allocating to a temporary slot.")
                        break

                    int_string = str(random_available_slot)
                    str_nums = []

                    for number in int_string:

                        if int(number) != 0:

                            get_double_digit = INT_TO_STRING_DOUBLE[int(str_nums[0])] + "0"

                            str_nums.clear()

                            slot_id = int("".join(str_nums))
                            
                        else: 
                            continue

                    double_digit = INT_TO_STRING_DOUBLE[int(str_nums[1])] + "0"

                    str_nums[0] = double_digit

                    slot_id = int("".join(str_nums))

                else:
                    # Randomize again if the chosen int is beyond the range, which is impossible but just in case
                    continue

                slots["slot_status"][random_available_slot] = "Active"
                slots["slot_status"][slot_id] = parse_memory # Assuming this also has the same format in json so they just be overwritten smoothly

                neuron_activated = True
                print(f"[{memory_holder.index(memory)+1}/100] Memory allocated to Neuron {random_available_neuron} (Attempts: {memory_operation_iterate})")

        asyncio.create_task(continue_transport(memory))
        memory_operation_iterate = 0

slots_watcher = watch("Slots.json", watch_filter=filter)