import React from "react"
import {Route, Routes, BrowserRouter} from "react-router-dom"
import NavBar from "./components/NavBar"
import './App.css';
/*pages */
import SignIn from "./pages/SignIn"
import RapProfilePage from "./pages/RapProfilePage"
import LandingPage from "./pages/LandingPage"
import APItest from "./pages/APItest"
function App() {   
    
    return (
        <BrowserRouter>
            <div>
                <div className="App">
                    <NavBar user={userType}/>
                    <div>
                        <Routes>
                            {/* add routes, unordered atm */}
                            <Route path="/" element={<APItest />} />  
                            <Route path="/LandingPage" element={<LandingPage />} />  
                            <Route path="/SignUp" element={<SignUp />} /> 
                            <Route path="/RapProfilePage" element={<RapProfilePage />} /> 
                            <Route path="/SignUp" element={<CustomerSignUp 
                                                                customer={dummyCustomer}
                                                                />} /> 
                            <Route path="/customerSubscriptionPayment" element={<CustomerSubPayment />} /> 
                            <Route path="/guestCustomerPayment" element={<GuestCustomerPayment />} /> 
                            <Route path="/MechanicSignUp" element={<MechanicSignUp />} /> 
                            <Route path="/MechanicHomePage" element={<MechanicHomePage />} /> 
                            <Route path="/CustomerProfile" element={<CustomerProfile />} /> 
                            <Route path="/MechanicSignIn" 
                                element={<MechanicSignIn changeUser={userType => setUserType(userType)}
                                                        mech = {dummyMechanic}/>} /> 

                            <Route path="/PlansAndPrices" element={<PlansAndPrices/>} />

                        </Routes>
                    </div>
                </div>
                
            </div>
        </BrowserRouter>
    
    )

}
export default App;

        
    
