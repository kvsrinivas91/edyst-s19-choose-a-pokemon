const express=require('express');
const app=express();
const data={
    "pokemon":["bulbasaur","charmander","squirtle"]
}
app.get('/api/pokemon',(req,res)=>{
res.send(data);
})

app.listen(8006,()=>{console.log('on 8006')})