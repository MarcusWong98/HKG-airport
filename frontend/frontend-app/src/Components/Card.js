import React,{useState, useEffect} from 'react'
import fetch_flights from '../functions'
import { Button, Pagination, Table } from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'


export default function Card() {

    const tHeaders = ['cargo', 'date', 'destination', 'airline', 'status']


    const [flights, setFlights] = useState({})

    useEffect(() => {

        const data = fetch_flights('GET')

        const flight_data = {
            'cargo': data['cargo'],
            'date': data['date'],
            // 'destination': data['flights']
        }

        setFlights([data])

    }, {})


    return (
        <div style = {{width: 80 + 'vw', margin: 'auto'}}>
            <Table responsive>
                <thead>
                    <tr id = 'airline-headers'>
                        {tHeaders.map(tHeader => <th>{tHeader.replace(tHeader[0], tHeader[0].toUpperCase()) }</th>)}
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>123</td>
                        <td>123</td>
                        <td>123</td>
                        <td>123</td>
                    </tr>
                    <tr>
                        <td>123</td>
                        <td>123</td>
                        <td>123</td>
                        <td>123</td>
                    </tr>
                </tbody>
            </Table>
            <Pagination style = {{width: '100%', justifyContent: 'center'} }>
                <Pagination.Item active = {'True'} >1</Pagination.Item>
                <Pagination.Item>2</Pagination.Item>
                <Pagination.Item>3</Pagination.Item>
            </Pagination>
            
        </div>
    )
}
