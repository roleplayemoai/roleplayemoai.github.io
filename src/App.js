import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import Footer from './components/Footer';
import { Container, Row, Col } from 'react-bootstrap';
import Home from './pages/Home';
import Scenario1 from './pages/Scenario1';
import Scenario2 from './pages/Scenario2';
import Scenario3 from './pages/Scenario3';
import Scenario4 from './pages/Scenario4';
import Scenario5 from './pages/Scenario5';
import Scenario6 from './pages/Scenario6';

function App() {
  return (
    <Router>
      <Container fluid>
        <Row>
          {/* Sidebar */}
          <Col xs={4} md={3} className="bg-light min-vh-100">
            <Sidebar />
          </Col>

          {/* Main Content */}
          <Col xs={8} md={9} className="p-4">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/scenario1" element={<Scenario1 />} />
              <Route path="/scenario2" element={<Scenario2 />} />
              <Route path="/scenario3" element={<Scenario3 />} />
              <Route path="/scenario4" element={<Scenario4 />} />
              <Route path="/scenario5" element={<Scenario5 />} />
              <Route path="/scenario6" element={<Scenario6 />} />
            </Routes>
            <Footer />
          </Col>
        </Row>
      </Container>
    </Router>
  );
}

export default App;
