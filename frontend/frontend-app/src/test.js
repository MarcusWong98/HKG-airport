import React, {useState, useEffect} from 'react'



export default function Test(){

    let data = ''

    useEffect(() => {
        
        fetch('/flights')
        .then(res => res.json())
        .then(data => console.log(data))

    })
    return(
        <div>{data}</div>
    )

}


