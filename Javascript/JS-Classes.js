const num = [1,2,3,4,5,6,7]
class MyName {
    constructor(name){
        this.name = name
        this.id= 1
    }
        yell(){
        console.log("ok..,I'm yelling !!")
        console.log(num)
    }
    display(){
        console.log(this.name)
        console.log(this.id)
    }
}
let obj =  new MyName("testName")
obj.yell()
