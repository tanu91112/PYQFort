# Solutions to NIT Kurukshetra CSIC 103 Question Paper (Dec 2023)

## Q1 (a) Check if a Number is the Sum of Two Prime Numbers (4 Marks)

**Logic/Algorithm**:
1. Input a number \( n \).
2. Define a function to check if a number is prime:
   - Check divisibility from 2 to \( \sqrt{n} \).
   - Return true if no divisors are found.
3. Iterate from \( i = 2 \) to \( n/2 \).
4. For each \( i \), check if \( i \) and \( n-i \) are prime.
5. If both are prime, print "Yes" and the pair; otherwise, print "No".

**Solution**:
```c
#include <stdio.h>
#include <math.h>
int isPrime(int num) {
    if (num <= 1) return 0;
    for (int i = 2; i <= sqrt(num); i++)
        if (num % i == 0) return 0;
    return 1;
}
int main() {
    int n, flag = 0;
    printf("Enter a number: ");
    scanf("%d", &n);
    for (int i = 2; i <= n / 2; i++) {
        if (isPrime(i) && isPrime(n - i)) {
            printf("Yes, %d can be expressed as %d + %d\n", n, i, n - i);
            flag = 1;
            break;
        }
    }
    if (!flag) printf("No, %d cannot be expressed as sum of two primes\n", n);
    return 0;
}
```
**Explanation**:
- The `isPrime` function checks primality efficiently using \( \sqrt{n} \).
- The main loop checks pairs \( (i, n-i) \). For example, for \( n = 7 \), it checks \( (2, 5) \), both prime, so outputs "Yes".
- For \( n = 11 \), no such pair exists, so outputs "No".
- **Marks**: 4 (1 for logic, 2 for code, 1 for correctness).

## Q1 (b) Interchange Elements of First and Last Columns in a Matrix (4 Marks)

**Logic/Algorithm**:
1. Input matrix dimensions \( r \) (rows) and \( c \) (columns).
2. Input the matrix elements.
3. For each row \( i \), swap elements at \( matrix[i][0] \) and \( matrix[i][c-1] \).
4. Print the modified matrix.

**Solution**:
```c
#include <stdio.h>
int main() {
    int r, c, i, j, temp;
    printf("Enter rows and columns: ");
    scanf("%d %d", &r, &c);
    int matrix[r][c];
    printf("Enter matrix elements:\n");
    for (i = 0; i < r; i++)
        for (j = 0; j < c; j++)
            scanf("%d", &matrix[i][j]);
    for (i = 0; i < r; i++) {
        temp = matrix[i][0];
        matrix[i][0] = matrix[i][c-1];
        matrix[i][c-1] = temp;
    }
    printf("Matrix after swapping first and last columns:\n");
    for (i = 0; i < r; i++) {
        for (j = 0; j < c; j++)
            printf("%d ", matrix[i][j]);
        printf("\n");
    }
    return 0;
}
```
**Explanation**:
- The program swaps the first (\( j=0 \)) and last (\( j=c-1 \)) columns for each row.
- For the example input:
  ```
  9 7 5
  2 3 4
  5 2 6
  ```
  Output is:
  ```
  5 7 9
  4 3 2
  6 2 5
  ```
- **Marks**: 4 (1 for logic, 2 for code, 1 for output format).

## Q1 (c) Calculate Electricity Units from Bill (4 Marks)

**Logic/Algorithm**:
1. Input the total bill amount.
2. Initialize units \( u = 0 \).
3. Calculate units based on slabs:
   - First 100 units: \( 1 \) rupee/unit.
   - 101–300 units: \( 2 \) rupees/unit.
   - 301–500 units: \( 5 \) rupees/unit.
   - Above 500: \( 10 \) rupees/unit.
4. Deduct bill amount slab-wise and increment units until the bill is exhausted.
5. Output the total units.

**Solution**:
```c
#include <stdio.h>
int main() {
    int bill, units = 0, temp;
    printf("Enter total bill: ");
    scanf("%d", &bill);
    temp = bill;
    if (temp > 0) {
        if (temp >= 100) {
            units += 100;
            temp -= 100;
        } else {
            units += temp;
            temp = 0;
        }
    }
    if (temp > 0) {
        if (temp >= 400) { // 200 units * 2
            units += 200;
            temp -= 400;
        } else {
            units += temp / 2;
            temp = 0;
        }
    }
    if (temp > 0) {
        if (temp >= 1000) { // 200 units * 5
            units += 200;
            temp -= 1000;
        } else {
            units += temp / 5;
            temp = 0;
        }
    }
    if (temp > 0) {
        units += temp / 10;
    }
    printf("Units consumed: %d\n", units);
    return 0;
}
```
**Explanation**:
- For bill = 1600:
  - 100 units at 1 = 100
  - 200 units at 2 = 400
  - 200 units at 5 = 1000
  - 10 units at 10 = 100
  - Total units = 510
- For bill = 120:
  - 100 units at 1 = 100
  - 10 units at 2 = 20
  - Total units = 110
- **Marks**: 4 (1 for logic, 2 for code, 1 for accuracy).

## Q1 (d) Swap 2nd and Last Digit of a Number (4 Marks)

**Logic/Algorithm**:
1. Input a positive integer \( n \).
2. Count digits and extract the last digit (using \( n \% 10 \)).
3. Extract the 2nd digit from the right by dividing \( n \) by 10 repeatedly until the 2nd position.
4. Compute the new number by:
   - Removing the 2nd and last digits.
   - Placing the last digit in the 2nd position and the 2nd digit in the last position.
5. Output the result.

**Solution**:
```c
#include <stdio.h>
#include <math.h>
int main() {
    int n, temp, digits = 0, last, second, i;
    printf("Enter a number: ");
    scanf("%d", &n);
    temp = n;
    last = n % 10;
    while (temp > 0) {
        digits++;
        temp /= 10;
    }
    temp = n / 10;
    second = temp % 10;
    int pos = digits - 2;
    int result = n - last - (second * pow(10, pos));
    result += second + (last * pow(10, pos));
    printf("Number after swapping: %d\n", result);
    return 0;
}
```
**Explanation**:
- For \( n = 12345 \):
  - Last digit = 5, 2nd digit = 4.
  - Digits = 5, so 2nd digit position = \( 10^{5-2} = 10^3 \).
  - Remove 5 and 4000, add 4 and 5000: \( 12345 - 5 - 4000 + 4 + 5000 = 42314 \).
- **Marks**: 4 (1 for logic, 2 for code, 1 for correctness).

## Q2 (a) Compare Two Doubles with Specified Precision (5 Marks)

**Logic/Algorithm**:
1. Input two doubles \( num1 \), \( num2 \), and precision \( s \).
2. Multiply both numbers by \( 10^s \) to shift digits.
3. Take the floor to compare up to \( s \) decimal places.
4. Return 0 if equal, 1 if \( num1 > num2 \), -1 otherwise.

**Solution**:
```c
#include <stdio.h>
#include <math.h>
int compare(double num1, double num2, int s) {
    long long n1 = floor(num1 * pow(10, s));
    long long n2 = floor(num2 * pow(10, s));
    if (n1 == n2) return 0;
    return n1 > n2 ? 1 : -1;
}
int main() {
    double num1, num2;
    int s;
    printf("Enter two numbers and precision: ");
    scanf("%lf %lf %d", &num1, &num2, &s);
    printf("Result: %d\n", compare(num1, num2, s));
    return 0;
}
```
**Explanation**:
- For \( num1 = 113.456052 \), \( num2 = 113.456059 \), \( s = 6 \):
  - \( 113.456052 \times 10^6 = 113456052 \), \( 113.456059 \times 10^6 = 113456059 \).
  - Since 113456052 < 113456059, return -1.
- For \( s = 5 \), both are 113456, so return 0.
- **Marks**: 5 (1 for logic, 3 for code, 1 for examples).

## Q2 (b) Check if R is a Perfect Power of r (5 Marks)

**Logic/Algorithm**:
1. Input \( n, m, N, M \) for \( r = n/m \), \( R = N/M \).
2. Check if \( R = r^k \) for some integer \( k \geq 0 \).
3. Simplify by checking \( N \times m^k = n^k \times M \).
4. Iterate \( k \) from 0 to a reasonable limit (e.g., 10).
5. Output "Perfect power" if true, else "Not a perfect power".

**Solution**:
```c
#include <stdio.h>
#include <math.h>
int main() {
    int n, m, N, M, k, flag = 0;
    printf("Enter n, m, N, M: ");
    scanf("%d %d %d %d", &n, &m, &N, &M);
    for (k = 0; k <= 10; k++) {
        if (N * pow(m, k) == pow(n, k) * M) {
            flag = 1;
            break;
        }
    }
    printf("%s\n", flag ? "Perfect power" : "Not a perfect power");
    return 0;
}
```
**Explanation**:
- For \( r = 2/3 \), \( R = 16/81 \):
  - Check \( 16 \times 3^k = 2^k \times 81 \).
  - For \( k = 4 \): \( 16 \times 81 = 1296 \), \( 2^4 \times 81 = 1296 \), true.
- For \( r = 4/3 \), \( R = 64/81 \), no \( k \) satisfies.
- **Marks**: 5 (1 for logic, 3 for code, 1 for accuracy).

## Q2 (c) Generate Sequence with Prime and Non-Prime Patterns (5 Marks)

**Logic/Algorithm**:
1. Input \( n \).
2. Define a function to check primality.
3. Generate sequence: 1 prime (2), 2 non-primes (4, 6), 3 primes (7, 11, 13), 4 non-primes (14, 15, 16, 18), etc.
4. Use a counter to track group size and type (prime/non-prime).
5. Output the first \( n \) terms.

**Solution**:
```c
#include <stdio.h>
#include <math.h>
int isPrime(int num) {
    if (num <= 1) return 0;
    for (int i = 2; i <= sqrt(num); i++)
        if (num % i == 0) return 0;
    return 1;
}
int main() {
    int n, count = 0, num = 2, group = 1, prime = 1;
    printf("Enter n: ");
    scanf("%d", &n);
    while (count < n) {
        int group_size = prime ? group : group + 1;
        for (int i = 0; i < group_size && count < n; num++) {
            if (prime && isPrime(num) || !prime && !isPrime(num)) {
                printf("%d ", num);
                count++;
                i++;
            }
        }
        prime = !prime;
        if (!prime) group++;
    }
    printf("\n");
    return 0;
}
```
**Explanation**:
- For \( n = 5 \): Output 2, 4, 6, 7, 11.
- For \( n = 10 \): Output 2, 4, 6, 7, 11, 13, 14, 15, 16, 18.
- Alternates between prime and non-prime groups, increasing group size.
- **Marks**: 5 (1 for logic, 3 for code, 1 for sequence).

## Q2 (d) Count Consecutive Vowels in a String (5 Marks)

**Logic/Algorithm**:
1. Input a string.
2. Iterate through the string, checking pairs of characters.
3. If both characters in a pair are vowels (a, e, i, o, u), increment counter.
4. Output the count.

**Solution**:
```c
#include <stdio.h>
#include <string.h>
int isVowel(char c) {
    c = tolower(c);
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}
int main() {
    char str[100];
    int count = 0;
    printf("Enter a string: ");
    fgets(str, 100, stdin);
    str[strcspn(str, "\n")] = 0; // Remove newline
    for (int i = 0; i < strlen(str) - 1; i++) {
        if (isVowel(str[i]) && isVowel(str[i + 1])) {
            count++;
        }
    }
    printf("Number of consecutive vowel pairs: %d\n", count);
    return 0;
}
```
**Explanation**:
- For "Please read this application and give me gratuity":
  - Pairs: ea (in "Please"), ea (in "read"), io (in "application"), ui (in "gratuity").
  - Output: 4.
- **Marks**: 5 (1 for logic, 3 for code, 1 for accuracy).

## Q3 (a) Read from Keyboard and Write to File (3 Marks)

**Logic/Algorithm**:
1. Open a file "abc.out" in write mode.
2. Read input from the keyboard until EOF (Ctrl+D/Ctrl+Z).
3. Write each input to the file.
4. Close the file.

**Solution**:
```c
#include <stdio.h>
int main() {
    FILE *fp = fopen("abc.out", "w");
    if (fp == NULL) {
        printf("Error opening file\n");
        return 1;
    }
    printf("Enter text (Ctrl+D to end):\n");
    char ch;
    while ((ch = getchar()) != EOF) {
        fputc(ch, fp);
    }
    fclose(fp);
    printf("Data written to abc.out\n");
    return 0;
}
```
**Explanation**:
- Uses `getchar()` for input and `fputc()` to write to the file.
- File is closed properly to ensure data is saved.
- **Marks**: 3 (1 for logic, 1 for code, 1 for file handling).

## Q3 (b) Structure for Automobile Parts and Retrieve Data (7 Marks)

**Logic/Algorithm**:
1. Define a structure with serial number, year, material, and quantity.
2. Input number of parts and their details.
3. Check if serial numbers are between "BB1" and "CC6" (lexicographically).
4. Display matching parts.

**Solution**:
```c
#include <stdio.h>
#include <string.h>
struct Part {
    char serial[4];
    int year;
    char material[20];
    int quantity;
};
int main() {
    int n;
    printf("Enter number of parts: ");
    scanf("%d", &n);
    struct Part parts[n];
    for (int i = 0; i < n; i++) {
        printf("Enter serial, year, material, quantity: ");
        scanf("%s %d %s %d", parts[i].serial, &parts[i].year, parts[i].material, &parts[i].quantity);
    }
    printf("Parts between BB1 and CC6:\n");
    for (int i = 0; i < n; i++) {
        if (strcmp(parts[i].serial, "BB1") >= 0 && strcmp(parts[i].serial, "CC6") <= 0) {
            printf("%s %d %s %d\n", parts[i].serial, parts[i].year, parts[i].material, parts[i].quantity);
        }
    }
    return 0;
}
```
**Explanation**:
- Structure `Part` stores required fields.
- `strcmp` ensures serial numbers are in range.
- **Marks**: 7 (2 for structure, 3 for input, 2 for retrieval).

## Q4 (a) Fill-in-the-Blank for Odd Numbers (4 Marks)

**Logic**:
- The loop prints numbers from 1 to 10, skipping even numbers.
- Condition: Skip if \( i \) is even (\( i \% 2 == 0 \)).

**Solution**:
The condition is: \( i \% 2 == 0 \).

**Explanation**:
- The loop runs from \( i = 1 \) to 10.
- If \( i \% 2 == 0 \), `continue` skips even numbers.
- Output: 1 3 5 7 9.
- **Marks**: 4 (2 for condition, 2 for explanation).

## Q4 (b) Output of Conditional Code (4 Marks)

**Solution**:
Output: Output1

**Explanation**:
- \( a = 100 \).
- First condition: \( a <= 100 \) is true, so prints "Output1".
- Other conditions are not evaluated.
- **Marks**: 4 (2 for output, 2 for explanation).

## Q4 (c) Output of Nested Ternary Operator (4 Marks)

**Solution**:
Output: 7

**Explanation**:
- \( a = 3 \), \( b = 7 \), \( c = 5 \).
- Ternary: \( d = a >= b ? (a >= c ? a : c) : (b >= c ? b : c) \).
- \( a >= b \) is false (3 < 7), so evaluate \( b >= c ? b : c \).
- \( b >= c \) is true (7 > 5), so \( d = b = 7 \).
- Printed in hexadecimal: \( 7 \).
- **Marks**: 4 (2 for output, 2 for explanation).

## Q4 (d) Output of Pointer Code (4 Marks)

**Solution**:
Output: 2

**Explanation**:
- Array \( a = \{1, 2, 3, 4, 5\} \), pointer \( p = a \).
- \( ++*p \) increments the value at \( p \), so \( a[0] = 2 \).
- \( *p \) accesses \( a[0] \), prints 2.
- **Marks**: 4 (2 for output, 2 for explanation).