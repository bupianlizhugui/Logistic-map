# Logistic-map


The logistic map is a polynomial mapping (equivalently, recurrence relation) of degree 2, often cited as an archetypal example of how **complex**, **chaotic** behaviour can arise from **very simple, non-linear** dynamic equations. (Read more at: 
[Wikipedia](https://en.wikipedia.org/wiki/Logistic_map),
[Wolfram](http://mathworld.wolfram.com/LogisticMap.html) )

 **The Recurrent Equation: X<sub>t+1</sub> = r*X<sub>t</sub>(1 - X<sub>t</sub> )**

To observe the dynamic behaviour, we initialised X with 0.1 and 0.1000000001 (Difference at 10<sup>th</sup> decimal position) and plug it into the above equation.

Below are the graphs that plot the change of values for both the inititialisations with different values of **r**.

For **r = 1**, there is hardly any variation, and irrespective of which value we start off with, it ultimately converges to a single value.
![alt text](https://github.com/yashchandak/Logistic-map/blob/master/images/r1.png )


For **r = 2**, we observe a similar behaviour, but it converges much quicker.
![alt text](https://github.com/yashchandak/Logistic-map/blob/master/images/r2.png )


By **r = 2.5**, slight fluctuations start building but then ulimately it stables down.
![alt text](https://github.com/yashchandak/Logistic-map/blob/master/images/r2.5.png )


Now begins the intersting part.
When we set **r = 3**, we start noticing a very periodic pattern. For both the initial starting points, we observe a very identical behaviour.
![alt text](https://github.com/yashchandak/Logistic-map/blob/master/images/r3.png )


On keeping **r = 3.25**, it quickly comes to point where it starts gracefully oscillating between two exact values.
![alt text](https://github.com/yashchandak/Logistic-map/blob/master/images/r3.25.png)


By **r = 3.5**, The points of oscillation double, and it now fluctuates periodically between 4 points.
![alt text](https://github.com/yashchandak/Logistic-map/blob/master/images/r3.5.png)


The chaotic behavior sets in by **r = 3.6**. Now there is hardly any fixed points between which it oscillates. Notice, that still it atleast displays similar behaviour for both the starting points.
![alt text](https://github.com/yashchandak/Logistic-map/blob/master/images/r3.6.png)


Here is the part where things start getting more interesting. Below is the graph for **r = 3.75**. Amusingly, even though the starting values differed in their 10<sup>th</sup> decimal place, after almost 50 iterations, there is hardly any correlation btween the values.
![alt text](https://github.com/yashchandak/Logistic-map/blob/master/images/r3.75.png )


For **r = 3.9**, The values start fluctuating even more.
![alt text](https://github.com/yashchandak/Logistic-map/blob/master/images/r3.9.png)


By the time we reach **r = 4**, it's a complete chaos. Both starting points display a completely different behaviour and there is hardly any similarity between them.
![alt text](https://github.com/yashchandak/Logistic-map/blob/master/images/r4.png )


The moment we try crossing **r = 4**,  something really goes weird and the values explode. Within a few iterations the values reach *infinity* and there is no turning back from there on. Furthermore, John Von Neumann had suggested using this equation with **r = 4** for random number generator in the late 1940s. 

#Does Deep-learning has anything to do with it?
Let's look at the recurrent equation again: **X<sub>t+1</sub> = r*X<sub>t</sub>(1 - X<sub>t</sub> )**. 
Doesn't it strongly resembles the derivative of the sigmoid activation? Moreover, setting the *learning hyper-parameter* effects the learning in a very similar fashion. The higher we set the learning rate, more is the fluctiation in the error rate;  And analogously on setting it beyond the certain value, the gradients explode and no learning takes place. Similarly, though the underlying mathematical model remains same, the starting values for the weights have a drastic impact on the overall training phase.

On the other hand, most of the current models now prefer using the ReLu function instead of the Sigmoid activation (to mitigate the vanishing gradient problem) and still display similar behaviour. **Is it just a matter of some simple co-incidence or is there really something intersting behind the hood?** 
