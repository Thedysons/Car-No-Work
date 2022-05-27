import React from "react"
import {Route, Routes, BrowserRouter} from "react-router-dom"
import NavBar from "./components/NavBar"
import './App.css';
/*pages */
import SignIn from "./pages/SignIn"
import RapProfilePage from "./pages/RapProfilePage"
import LandingPage from "./pages/LandingPage"
import CustomerSignUp from "./pages/CustomerSignUp";
import CustomerSubPayment from "./pages/CustomerSubPayment";
import GuestCustomerPayment from "./pages/GuestCustomerPayment";
import CustomerHome from "./pages/CustomerHome"
import MechanicSignIn from "./pages/MechanicSignIn";
import MechanicHomePage from "./pages/MechanicHomePage";


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
                            <Route path="/SignIn" element={<SignIn />} /> 
                            <Route path="/RapProfilePage" element={<RapProfilePage />} /> 
                            <Route path="/SignUp" element={<CustomerSignUp />} /> 
                            <Route path="/customerSubscriptionPayment" element={<CustomerSubPayment />} /> 
                            <Route path="/guestCustomerPayment" element={<GuestCustomerPayment />} /> 
                            <Route path="/CustomerHome" element={<CustomerHome />} />
                            <Route path="/MechanicSignIn" element={<MechanicSignIn />} /> 
                            <Route path="/MechanicHomePage" element={<MechanicHomePage />} /> 
                        </Routes>
                    </div>
                </div>
                
            </div>
        </BrowserRouter>
    
    )

}
export default App;

        
    
