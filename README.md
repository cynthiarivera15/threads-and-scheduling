# Project 1: Threads and Scheduling


University of Puerto Rico

Río Piedras Campus

Department of Computer Science

Student Name: Cynthia Marie Rivera Sánchez

Course & Section: CCOM4017-002

## Contents of this file
* Description of the program
* Instructions on how to execute the program
* References used to perform the program

## Description
This program contains the following two files: ```edevice.py``` and ```scheduler.py```.

The first file, ```edevice.py```, simulates the embedded devices which will be sending continuous messages to the scheduler between short intervals of time. Each message will contain the Device ID and a number which represent the amount of time the job will take.

The second file, ```scheduler.py```, contains only two threads the producer and the consumer. The producer will receive the messages sent by the devices and store them in a shared list simulating the Shortest Job First scheduling algorithm. The consumer, on the other hand, will remove the messages from the shared list and keep track of the amount of time each device has consume inside a dictionary.

## Instructions
To run the program you have to execute the ```scheduler.py``` file and the ```edevice.py``` file using ```python3```.

Now, there are three global variables in total which can be change by the user. The first two variables con be found on the ```edevice.py``` file. These are: ```MAX_CPU_RANGE``` which will represent the maximum amount of time a job can take and ```devices``` which will be the amount of devices sending messages to the scheduler. The last variables is found on the ```scheduler.py``` and it is ```N```. This variable represents the amount of jobs the scheduler will be able to perform.

Once both files are running, the ```edevice.py``` file will create threads which will be sending messages through a socket to the producer. The producer will receive the message, grab the device id and the amount of time consume by it and store it in a shared list (this will happen N times). At the same time the producer is storing messages in the list, the consumer will be removing those messages and storing the total amount of time each job is taking in a dictionary (this will also happen N times). Once the consumer has remove the Nth message, the ```scheduler.py``` file will have as an output each device id and the total amount of time each device consumed.

Note: Even when the scheduler has finished, the devices will keep sending messages
Note: To prevent a race condition from happening, since both the inserting and removing part formed part of the critical region they were protected by using semaphores.

## References
To do this program multiple references where used:
* How to send messages using sockets: https://pythontic.com/modules/socket/udp-client-server-example
* Removing characters from strings: https://www.journaldev.com/23674/python-remove-character-from-string
* Dividing strings: https://www.geeksforgeeks.org/python-string-split/
* Converting a list of strings into ints: https://www.kite.com/python/answers/how-to-convert-a-list-of-strings-to-ints-in-python
* Doing a dictionary: https://www.tutorialspoint.com/python/dictionary_get.htm & https://www.kite.com/python/answers/how-to-change-a-dictionary-value-in-python
* How to iterate through a dictionary: https://realpython.com/iterate-through-dictionary-python/
* How to do a ReadMe file: https://www.drupal.org/docs/develop/managing-a-drupalorg-theme-module-or-distribution-project/documenting-your-project/readme-template

Also the student Joniel Méndez helped fix some problems the ```Organize(msg)``` function was presenting
