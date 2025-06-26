# Load built-in dataset
data(mtcars)
data(iris)

# View structure
str(mtcars)
str(iris)

# Summary statistics
summary(mtcars)
summary(iris)

# Base R plot for mtcars
plot(mtcars$wt, mtcars$mpg, main="MPG vs Weight", xlab="Weight", ylab="MPG")

# Base R plot for iris
plot(iris$Petal.Length ~ iris$Petal.Width, col=iris$Species)

# Step 2: Build the linear regression model
model1 <- lm(mpg ~ wt + hp, data = mtcars)

# Step 3: Create new data for prediction
newdata <- data.frame(wt = 3, hp = 110)

# Step 4: Predict mpg
predict(model1, newdata)

# Plot with regression line
plot(mtcars$wt, mtcars$mpg)
abline(model1, col="red")