import React from "react"
import { FaStar } from "react-icons/fa"

export default function RapProfilePage() {
    return (
        <div className= "pageBackground">
            <div className="pageLayout">
                <h1>Mechanic Name</h1>
                <div className="RapPhoto"></div>
                <div className="Rating">
                    <FaStar className = "Star"/>
                    <FaStar className = "Star" />
                    <FaStar className = "Star" />
                    <FaStar className = "Star"/>
                    <FaStar className = "Star" />
                </div>
                <button>See Reviews</button>
                <div className="infoHold">
                    <div className="RapInfoLabel">
                        <p>Car:</p>
                        <p>LicencePlate:</p>
                        <p>Date of Birth:</p>
                        <p>Date Started:</p>
                    </div>
                </div>

                <button>Job History</button>
                <button>Job Requests</button>
            </div>
        </div>
    )
}