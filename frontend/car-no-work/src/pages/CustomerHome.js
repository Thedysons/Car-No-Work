import React from "react"
import {TiTick} from "react-icons/ti"
export default function CustomerHome() {
    return (
        <div className = "pageBackground">
            <div className ="pageLayout">
                <h1>Home</h1>
                <h3 className="homeCusName">(Customer Name)</h3>
                
                    <p className= "crashDetsLabel">Enter Crash Details(500 characters)</p>
                    <textarea rows= "10" className="crashDetails"></textarea>
                    <div className ="requestService">                   
                            <button className="serviceButton">Request Service</button>
                            <p className= "serviceSent"><TiTick className ="test"/></p>                    
                    </div>
                    <p className="CusHomeLabel">distance: </p>
                    <p className="CusHomeLabel">time:</p>
                
            </div>
        </div>
    )
}