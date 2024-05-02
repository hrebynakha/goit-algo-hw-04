# Home work 3
Install requirements
```
pip install -r requirements.txt
```
run `py hw4.py`

Вивід результатів сортування, при парметрах
- кількість тестів функції 5000 разів
- масив даних 2000 елементів
- масиви даних мають різну структуру (сортовані, частково сортовані, і не сортовані)

```

Testing function merge for array:sorted ....
Function: merge sort array: sorted elapsed time:20.510304699884728
Testing function merge for array:not_sorted ....
Function: merge sort array: not_sorted elapsed time:25.618881500093266
Testing function merge for array:part_sorted ....
Function: merge sort array: part_sorted elapsed time:22.41003859997727
Testing function insertion for array:sorted ....
Function: insertion sort array: sorted elapsed time:1.2969314998481423
Testing function insertion for array:not_sorted ....
Function: insertion sort array: not_sorted elapsed time:1.4232489001005888
Testing function insertion for array:part_sorted ....
Function: insertion sort array: part_sorted elapsed time:1.3257681999821216
Testing function timsort for array:sorted ....
Function: timsort sort array: sorted elapsed time:0.058548400178551674
Testing function timsort for array:not_sorted ....
Function: timsort sort array: not_sorted elapsed time:0.06244260002858937
Testing function timsort for array:part_sorted ....
Function: timsort sort array: part_sorted elapsed time:0.060378999914973974

```

Можемо зробити висновок, що функція сортування злиттям (merge sort) є найменшефективнішою,
при будь яких введених даних, функція буде проходить цикл по всім даним.