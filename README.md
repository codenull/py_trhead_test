# py_thread_test
��������� ��������������� � ������������� ��������� � python3.

# ������
* ������� ���������� ������� ������.
* ��������� ���� ������ ���������.
* ��������� �� ����� ������� � ��� ������ ������ ������� ����� �������� �� �������:
```
arr[i] = (arr[i] * Math.sin(0.2f + i / 5) * Math.cos(0.2f + i / 5) * Math.cos(0.4f + i / 2))
```
* ���������� ������� �� ������� ����� ��������� � ��������� �������.

# ���������
## Thread
```
Len: 10000000. Threads: 1. Time: 6521.
Len: 10000000. Threads: 2. Time: 6680.
Len: 10000000. Threads: 4. Time: 6606.
Len: 10000000. Threads: 10. Time: 6646.
Len: 10000000. Threads: 20. Time: 6763.
```

## Process
```
Len: 10000000. Threads: 1. Time: 6639.
Len: 10000000. Threads: 2. Time: 3647.
Len: 10000000. Threads: 4. Time: 2319.
Len: 10000000. Threads: 10. Time: 2307.
Len: 10000000. Threads: 20. Time: 3338.
```