
# What Are Your Chances Of Winning The US Open?

These riddler challenges were posted on the 538 site on September 6, 2019 [here](https://fivethirtyeight.com/features/what-are-your-chances-of-winning-the-u-s-open/).

---

## Riddler Classic

The classic riddle states the object of the two player game “Acchi, Muite, Hoi” where one player points to a direction (up, down, left, right) and the other player has to look at one of those directions at the same time. If they point/look at the same direction, they win, if not they switch roles and play again. It then asks the probability of you winning the game.

To solve this I believe we only need a basic understanding of probability. If we set the direction as absolute e.g. N, S, E, W, and we take the players choices to be truley random and not just psuedorandom, we can easily predict the probability of the outcome. 

There are four choices to choose from, so the probability of each player picking each choice is $\frac{1}{4}$.

The chances of both people picking a certain set of direction (i.e. both picking the same direction and winning) is therefore $\frac{1}{4} \times \frac{1}{4} = \frac{1}{16} = 6.25\%$


```python

```
