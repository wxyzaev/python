# 02장 파이썬 프로그래밍의 기초, 자료형

[점프 투 파이썬 / 02장 파이썬 프로그래밍의 기초, 자료형](https://wikidocs.net/11)

<br/>

## 자료형 (Data Type)
* 프로그래밍을 할 때 쓰이는 숫자, 문자열 등 자료 형태로 사용하는 모든 것
* 프로그램의 기본이자 핵심 단위

<br/>

## 02-1 숫자형 (Number)

### 숫자형이란?
* 숫자 형태로 이루어진 자료형

    | 항목   | 사용 예                 |
    | ------ | ----------------------- |
    | 정수   | 123, -345, 0            |
    | 실수   | 123.45, -1234.5, 3.4e10 |
    | 8진수  | 0o34, 0o25              |
    | 16진수 | 0x2A, 0xFF              |

<br/>

### 숫자형은 어떻게 만들고 사용할까?
+ 정수형 (Integer)

    ```python
    >>> a = 123
    >>> a = -178
    >>> a = 0
    ```

<br/>

+ 실수형 (Floating-point)

    ```python
    >>> a = 1.2
    >>> a = -3.45
    >>> a = 4.24e10
    >>> a = 4.24e-10
    ```

<br/>

+ 8진수와 16진수
    - 8진수 (Octal) : 0o 로 시작
    - 16진수 (Hexadecimal) : 0x 로 시작
    
        ```python
        >>> a = 0o15
        >>> b = 0xFF
        ```

<br/>

### 숫자형을 활용하기 위한 연산자
+ 사칙연산

    ```python
    >>> a = 3
    >>> b = 4
    >>> a + b
    7
    >>> a - b
    -1
    >>> a * b
    12
    >>> a / b
    0.75
    ```

<br/>

+ x의 y제곱을 나타내는 `**` 연산자
    - `x**y` : x의 y제곱
    
        ```python
        >>> a = 3
        >>> b = 4
        >>> a ** b
        81
        ```

<br/>

+ 나눗셈 후 나머지를 반환하는 `%` 연산자

    ```python
    >>> 7 % 3
    1
    >>> 3 % 7
    3
    ```

<br/>

+ 나눗셈 후 몫을를 반환하는 `//` 연산자

    ```python
    >>> 7 // 4
    1
    ```
