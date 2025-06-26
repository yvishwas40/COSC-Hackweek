# Load datasets
data(mtcars)
data(iris)

# Regression model on mtcars
model1 <- lm(mpg ~ wt + hp, data = mtcars)
plot(mtcars$wt, mtcars$mpg, main="MPG vs Weight", xlab="Weight", ylab="MPG")
abline(lm(mpg ~ wt, data = mtcars), col="red")  # add regression line

# Regression model on iris
model2 <- lm(Petal.Length ~ Petal.Width, data = iris)
plot(iris$Petal.Width, iris$Petal.Length, col=iris$Species,
     main="Petal Length vs Width", xlab="Petal Width", ylab="Petal Length")
abline(model2, col="blue", lwd=2)  # add regression line

# Optional prediction
predict(model1, data.frame(wt=3, hp=110))
predict(model2, data.frame(Petal.Width=1.5))
