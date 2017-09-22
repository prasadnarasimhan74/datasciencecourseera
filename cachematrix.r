## Put comments here that give an overall description of what your
## functions do
# makeCacheMatrix creates a list containing a function to
# 1. set the value of the matrix
# 2. get the value of the matrix
# 3. set the value of inverse of the matrix
# 4. get the value of inverse of the matrix

makeCacheMatrix <- function(x = matrix()) {
  
  inverse <- NULL
  
  set <- function(param){
    x <<- param
    inverse <<- NULL
  }
  get <- function() x
  setinverse <- function(paramInverse)inverse=paramInverse
  getinverse <- function() inverse
  list(set=set,get=get,setinverse=setinverse,getinverse=getinverse)
}

# The function returns the inverse of the matrix. At first it checks whether
# the inverse has already been computed. If so, it returns the result . 
# if not, it computes the inverse, sets the value in the cache via
# setinverse function.

cacheSolve <- function(x, ...) {
        ## Return a matrix that is the inverse of 'x'
        inverse <- x$getinverse()
        
        if(!isnull|(inverse)){
          return(inverse)
        }
        data <- x$get()
        inverse <- solve(data)
        x$setinverse(inverse)
        inverse
}
