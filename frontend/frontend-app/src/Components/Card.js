import React,{useState, useEffect} from 'react'
import fetch_flights from '../functions'
import {Button} from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'


export default function Card() {


    const [flights, setFlights] = useState([]) 

    useEffect(() => {

        const data = fetch_flights('GET')        

        setFlights(['test'])

    }, flights)


    return (
        <Button>Test</Button>
    )
}
