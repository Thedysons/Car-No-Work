import React from "react"
import {useNavigate} from "react-router-dom"
export default function CustomerHome(props) {
    const navigate = useNavigate()
    
    function openRAP() {
        navigate("/RapProfilePage")
    }
    

    return (
        <div className = "pageBackground">
            <div className ="pageLayout">
                <h1>Home</h1>
                <h3 className="homeCusName">(Customer Name)</h3>
                
                    <p className= "crashDetsLabel">Enter Crash Details(500 characters)</p>
                    <textarea rows= "10" className="crashDetails"></textarea>
                    <div className ="requestService">                   
                            <button className="serviceButton">Request Service</button>
                            <div className= "lblHolder">
                                <div className= "driverAcceptedDisplay">Driver Accepted</div>
                                <p className="CusHomeLabel">Distance: </p>
                                <p className="CusHomeLabel">Time:</p> 
                                <p className="CusHomeLabel">Number Plate:</p>                                 
                            </div>                                                                      
                    </div>                    
                    <button className = "driverDetails" onClick={openRAP}>See Driver Details</button>  
            </div>
        </div>
    )
}