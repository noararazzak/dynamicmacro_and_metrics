
# Practice
x=seq(-3,3,0.01)
y=dnorm(x)
plot(x,y,type = "l")
yy=(1/sqrt(2))*dnorm(x/sqrt(2))
lines(x,yy)

# Problem 1
x=seq(-5,5,0.01)
y=dnorm(x,0,1)
plot(x,y,type = "l", xlim=c(-5,5),ylim=c(0,1.5), col = "red")
y1=dnorm(x,0,3)
y2=dnorm(x,0,0.333)
lines(x,y1, col = "green")
lines(x,y2, col = "cyan")

legend("topright", legend=c("normal mean=0 std=1", "normal mean=0 std=3", "normal mean=0 std=1/3" ),
       fill=c("red","green", "cyan"))

# Problem 2
x=seq(-5,5,0.01)

# Normal with mean 0 and std dev 1

y=dnorm(x,0,1)
plot(x,y,type = "l", xlim=c(-5,5),ylim=c(0,0.8), col = "red")

# Weibull Shape beta = 3.45 and Scale alpha = 3.34

###
# Your "shape" and "scale" parameters are correct, but you input the wrong mean.
###

#y1=dweibull(x-3, 3.45, 3.34, log = FALSE)
mu = -3
y1=dweibull(x-mu, 3.45, 3.34, log = FALSE)
lines(x,y1, col = "green")

legend("topright", legend=c("normal mean=1 std=1", "weibull mean = -3 alpha=3.34 beta=3.45"),
       fill=c("red","green"))

#Problem 3

# Weibull Shape = beta and Scale = alpha
x=seq(0,8,0.01)
y1=dweibull(x, 1, 1, log = FALSE)
plot(x, y1, type = "l", xlim=c(0,8),ylim=c(0,2), col = "red")
y2=dweibull(x, 2, 1, log = FALSE)
lines(x,y2, col = "green")
y3=dweibull(x, 3, 2, log = FALSE)
lines(x,y3, col = "cyan")
y4=dweibull(x, 5, 4, log = FALSE)
lines(x,y4, col = "dimgrey")
y5=dweibull(x, 9, 6, log = FALSE)
lines(x,y5, col = "blue")
y6=dweibull(x, 16, 7, log = FALSE)
lines(x,y6, col = "deeppink")

legend("topright", legend=c("weibull alpha=1 beta=1", "weibull alpha=1 beta=2", "weibull alpha=3 beta=2", "weibull alpha=5 beta=4","weibull alpha=9 beta=6","weibull alpha=16 beta=7"),
       fill=c("red","green", "cyan", "dimgrey", "blue", "deeppink"))

#Problem 4

# Beta Shape1 = alpha and Shape2 = beta
x=seq(0,1,0.01)
y1=dbeta(x, 1, 4, log = FALSE)
plot(x, y1, type = "l", xlim=c(0,1),ylim=c(0,7), col = "red")
y2=dbeta(x, 2, 4, log = FALSE)
lines(x,y2, col = "green")
y3=dbeta(x, 14, 14, log = FALSE)
lines(x,y3, col = "cyan")
y4=dbeta(x, 6, 6, log = FALSE)
lines(x,y4, col = "dimgrey")
y5=dbeta(x, 4, 2, log = FALSE)
lines(x,y5, col = "blue")
y6=dbeta(x, 4, 1, log = FALSE)
lines(x,y6, col = "deeppink")
legend("topright", legend=c("beta alpha=1 beta=4", "beta alpha=2 beta=4", "beta alpha=14 beta=14", "beta alpha=6 beta=6","beta alpha=4 beta=2","beta alpha=4 beta=1"),
       fill=c("red","green", "cyan", "dimgrey", "blue", "deeppink"))

#Problem 5

# Gamma Shape = alpha and Scale = beta
x=seq(0,14,0.01)

###
# NOTE THAT dgamma(x, shape, rate = 1, scale = 1/rate, log = FALSE). 
# You assigned beta values into "rate", so you might want to explicitly put the argument names "shape" and "scale".
###

#y1=dgamma(x, 1, 1, log = FALSE)
y1=dgamma(x, shape = 1, scale = 1, log = FALSE)
plot(x, y1, type = "l", xlim=c(0,14),ylim=c(0,2), col = "red")
#y2=dgamma(x, 1, 2, log = FALSE)
y2=dgamma(x, 1, scale = 2, log = FALSE)
lines(x,y2, col = "green")
#y3=dgamma(x, 1, 3, log = FALSE)
y3=dgamma(x, 1, scale =3, log = FALSE)
lines(x,y3, col = "cyan")
#y4=dgamma(x, 1, 5, log = FALSE)
y4=dgamma(x, 1, scale =5, log = FALSE)
lines(x,y4, col = "dimgrey")
#y5=dgamma(x, 1, 8, log = FALSE)
y5=dgamma(x, 1, scale =8, log = FALSE)
lines(x,y5, col = "blue")

legend("topright", legend=c("gamma alpha=1 beta=1", "gamma alpha=1 beta=2", "gamma alpha=1 beta=3", "gamma alpha=1 beta=5","gamma alpha=1 beta=8"),
       fill=c("red","green", "cyan", "dimgrey", "blue"))




