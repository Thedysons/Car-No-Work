import React from "react"
import {Route, Routes, BrowserRouter} from "react-router-dom"
import NavBar from "./components/NavBar"
import './App.css';
/*pages */
import SignUp from "./pages/SignUp"
import RapProfilePage from "./pages/RapProfilePage"
import LandingPage from "./pages/LandingPage"
import CustomerSignUp from "./pages/CustomerSignUp";
import CustomerSubPayment from "./pages/CustomerSubPayment";



function App() {  
        
    return (
        <BrowserRouter>
            <div>
                <div className="App">
                    <NavBar/>
                    <div>
                        <Routes>
                            {/* add routes, unordered atm */}
                            <Route path="/" element={<RapProfilePage />} />  
                            <Route path="/LandingPage" element={<LandingPage />} />  
                            <Route path="/SignIn" element={<SignUp />} /> 
                            <Route path="/RapProfilePage" element={<RapProfilePage />} /> 
                            <Route path="/customerSignUp" element={<CustomerSignUp />} /> 
                            <Route path="/customerSubscriptionPayment" element={<CustomerSubPayment />} /> 
                        </Routes>
                    </div>
                </div>
                
            </div>
        </BrowserRouter>
    
    )

}
export default App;

        
    
