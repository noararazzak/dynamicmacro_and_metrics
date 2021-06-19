#Practice
z=rbeta(100,2,2)
par(lty=1)
plot(density(z),main="Beta Distribition",xlim=c(-4,4),ylim=c(0,1.8), col = "blue")
par(lty=2)
zz=seq(-4,4,0.001)
lines(zz,dnorm(zz),type="l", col = "red")
legend("topleft",c("zz","Beta Distribution"),fill=c("red","blue"))

#Practice 2
x <- runif(20, -1, 1)
v = mean(x)
print(v)

#Practice 2
x <- rexp(100, rate =2)
v = mean(x)
print(v)

#Practice 3
x=seq(-1,1,0.1)
truedist = .8*dnorm(x,0,1) + .15*dnorm(x,1000,10) + .05*dnorm(x,1000000,1000)
truem = mean(truedist)
truesd =sd(truedist)
print (truem)
print (truesd)
plot(density(truedist), main="Actual Distribition of Mixture Normal", xlab = "X", ylab = "f(x)", col = "blue")

#Practice 4

number <- 100000
components <- sample(1:3,prob=c(0.8,0.15,0.05),size=number,replace=TRUE)
mus <- c(0,1000,1000000)
sds <- sqrt(c(1,10,1000))

samples <- rnorm(n=number,mean=mus[components],sd=sds[components])

print(samples)
plot(density(samples), main="Simulated Distribition from Mixture Normal", xlab = "X", ylab = "f(x)", col = "blue")
print (mean(samples))
print(sd(samples))

#Practice 5

findnormdensity <- function(n)
{
  anslist <- vector(mode = "list", length = 2)
  addition <- 0
  unidist = runif(n, 0, 1)
  distribution = as.numeric(vector(length=n))
  for(i in 1:n){
    if(unidist[i]<0.05){
      distribution[i] = rnorm(1, 1000000, sqrt(1000))
    } else if(unidist[i]<0.20){
      distribution[i] = rnorm(1, 1000, sqrt(10))
    } else {
      distribution[i] = rnorm(1, 0, 1)
    }
    addition = addition + distribution[i]
    
  }
  meandist = addition/n
  return (distribution)
  
  
}

plot(density(findnormdensity(100000)), main="Simulated Distribition from Mixture Normal 2", xlab = "X", ylab = "f(x)", col = "blue")
print(mean(findnormdensity(100000)))
print (sd(findnormdensity(100000)))
#Problem 1 a, b, c and d
#Notice that the variable n was changed each time where n = [5,10,50,100]


N = 1000
n = 100
dist = vector(length = N)
for (i in 1:N)
{
  x <- runif(n, -1, 1)
  v =  mean(x)
  dist[i] = sqrt(n)* (v - 0)/0.5774
}

par(lty=1)
plot(density(dist),main="Simulated Distribition",xlab = "X", ylab = "f(x)", xlim=c(-4,4),ylim=c(0,0.6), col = "blue")
par(lty=2)
z=seq(-4,4,0.001)
lines(z,dnorm(z),type="l", col = "red")
legend("topright",c("Normal Distribution (0,1)","Simulated Distribution"),fill=c("red","blue"))


#Problem 2 a, b, c and d
#Notice that the variable n was changed each time where n = [5,10,50,100]


N = 1000
n = 100
dist = vector(length = N)
for (i in 1:N)
{
  x <- rexp(n, rate = 2)
  v =  mean(x)
  dist[i] = sqrt(n)* (v - 0.5)/0.5
}

par(lty=1)
plot(density(dist),main="Simulated Distribition",xlab = "X", ylab = "f(x)",xlim=c(-4,4),ylim=c(0,0.8), col = "blue")
par(lty=2)
z=seq(-4,4,0.001)
lines(z,dnorm(z),type="l", col = "red")
legend("topright",c("Normal Distribution (0,1)","Simulated Distribution"),fill=c("red","blue"))

#Problem 3 a, b, c and d
#Notice that the variable n was changed each time where number = [5,10,50,100]
#The standard deviation is approximated using Practice 5 to be 215961.7




N = 1000
number= 500
x=seq(-1,1,0.01)
truedist = .8*dnorm(x,0,1) + .15*dnorm(x,1000,10) + .05*dnorm(x,1000000,1000)
truem = .8*0 + 0.15*1000 + .05*1000000 
print (truem)
dist = as.numeric(vector(length = N))
for (i in 1:N)
{
  components <- sample(1:3,prob=c(0.8,0.15,0.05),size=number,replace=TRUE)
  mus <- c(0,1000,1000000)
  sds <- sqrt(c(1,10,1000))
  
  samples <- rnorm(n=number,mean=mus[components],sd=sds[components])
  
  v= mean(samples)
  dist[i] = sqrt(number)* (v - truem)/217125.6
  
}

sapply(dist, typeof)
print(dist)
par(lty=1)
plot(density(dist),main="Simulated Distribition",xlab = "X", ylab = "f(x)",xlim=c(-4,4),ylim=c(0,1.5), col = "blue")
par(lty=2)
z=seq(-4,4,0.01)
lines(z,dnorm(z),type="l", col = "red")
legend("topright",c("Normal Distribution (0,1)","Simulated Distribution"),fill=c("red","blue"))