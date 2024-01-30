# About

This is a caesar encryption program that will shift the letters by some k amount to the right. An example is 'abc' can be shifted by 3 will be 'def'. 

The program takes two arguments the string and the number that it is shifting the string by.

```
python3 caesar.py abc 3
```

This will return an output of the encrypted and decrypted word.

If incrementing by a larger number than 26 will result in rolling over the letter back from a. An example of rolling over the numbers is the following...

```
python3 caesar.py abcz 3 
```

this will result with the encrypted word being 'defc' where the last letter is seen to roll back to a and increased to c.