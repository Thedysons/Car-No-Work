import React from "react"
import {Route, Routes, BrowserRouter} from "react-router-dom"
/*pages */
import SignUp from "./pages/SignUp"
import RapProfilePage from "./pages/RapProfilePage"
import LandingPage from "./pages/LandingPage"
function App() {   
    return (
        <BrowserRouter>
            <div>
                <Routes>
                    {/* add routes, unordered atm */}
                    <Route path="/" element={<RapProfilePage />} />  
                    <Route path="/LandingPage" element={<LandingPage />} />  
                    <Route path="/SignUp" element={<SignUp />} /> 
                </Routes>
            </div>
        </BrowserRouter>
    
    )
}
export default App;