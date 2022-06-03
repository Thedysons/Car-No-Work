import React from "react"
import Logo from "../img/logoTransBlack.png"

export default function MechanicHomePage() {
    return (
        <div className="pageBackground">
            <div className="pageLayout">                
                <h1>Mechanic home</h1>
                <div>
                    <p>(List of requests)</p>
                </div>
                <div className="mechHomeButtonLayout">
                    <button className="submitButton">Accept Request</button>
                    <button className="submitButton">Deny Request</button>
                </div>
            </div>
        </div>
    )
}