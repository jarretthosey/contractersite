import React, { Component } from 'react'
import { BrowserRouter, Route } from 'react-router-dom'
import './App.css'
import HomePage from './pages/HomePage.js'
import AdminHome from './pages/AdminHome.js'
import Pay from './pages/Pay.js'

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <div>
          <Route exact path="/" component={HomePage} />
          <Route exact path="/admin" component={AdminHome} />
          <Route exact path="/pay" component={Pay} />
        </div>
      </BrowserRouter>
    </div>
  );
}

export default App;
