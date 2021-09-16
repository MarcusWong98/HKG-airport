// export class Flight{
//     constructor(cargo, date, destination, airline, status){
//         this.cargo = cargo,
//         this.date = date,
//         this.destination = destination,
//         this.airline = airline,
//         this.status = status
//     }
// }

export const Flight = (cargo, date, destination, airline, status) => {
    return {
        'cargo': cargo,
        'date': date,
        'destination': destination,
        'airline': airline,
        'status': status
    }
}