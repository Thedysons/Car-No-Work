import React from "react"
import him from "../img/8f894a44e3cd1a595d547670308eae36.png"
import { Link } from "react-router-dom"
export default function CustomerProfile() {
    return (
        <div className= "pageBackground">
            <div className="pageLayout">
                <h1>Customer Name</h1>
                <img src={him} className="RapPhoto" alt='him'/>
                
                <div className="infoHold">
                    <div className="cusInfoLabel">
                        <p>Car:</p>
                        <p>Num Of Rquests:</p>
                        <p>Date of Birth:</p>                        
                    </div>
                </div>

                <button className="submitButton">Claim History</button>                                   
               
            </div>
        </div>
    )
}