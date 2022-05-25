import React from "react"
import { FaStar } from "react-icons/fa"
import him from '../img/8f894a44e3cd1a595d547670308eae36.png';

export default function RapProfilePage() {
    return (
        <div className= "pageBackground">
            <div className="pageLayout">
                <h1>Mechanic Name</h1>
                <img src={him} className="RapPhoto" alt='him'/>
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