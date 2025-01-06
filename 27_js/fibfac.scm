//Team TJMax :: Tracy Ye, Jessica Yu
//SoftDev pd5
//K27 - Basic functions in JavaScript
//2025-01-06m

#lang racket

(define fact(lambda(n)
  (if (= n 1)
      1
      (* n fact(- n 1)))))

(fact 1);


(define fib(lambda(n)
  (if (= n 0)
      0
      (if (= n 1)
          1
          (+ (fib(- n 1)) (fib(- n 2)))))))

(fib 0); // 0
(fib 1); // 1
(fib 2); // 1
(fib 3); // 2
(fib 4); // 3
(fib 5); // 5
(fib 6); // 8