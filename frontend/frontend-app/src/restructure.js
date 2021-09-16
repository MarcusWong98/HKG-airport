import {Flight} from "./Classes";



export default function restructure(data){

    const flight_array = []

    console.log(data)

    data['flights'].forEach(flight => {

        console.log(flight)
        const f = Flight(
            data['cargo'],
            data['date'],
            flight['destination'],
            data['flights'].length,
            flight['status']
        )
        flights.append(f)
    });
    return flight_array
}

// this.cargo = cargo,
// this.date = date,
// this.destination = destination,
// this.airline = airline,
// this.status = status