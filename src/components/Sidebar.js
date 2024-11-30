import React from 'react';
import { Nav } from 'react-bootstrap';
import { Link } from 'react-router-dom';

function Sidebar() {
  return (
    <Nav className="flex-column p-3">
      <Nav.Link href="/" className="text-dark">EmoAI Ethics: Guidelines and Resouces</Nav.Link>
      <hr />
      <Nav.Link as={Link} to="/scenario1" className="text-dark">
        1 <b>HR Company</b> - Concerns Regarding Potential Gender Bias in Emotion AI Software
      </Nav.Link>
      <Nav.Link as={Link} to="/scenario2" className="text-dark">
        2 <b>Leading IT Company</b> - Proposal for Collaboration on Emotion AI for Internal Assessment
      </Nav.Link>
      <Nav.Link as={Link} to="/scenario3" className="text-dark">
        3 <b>Digital Healthcare Provider</b> - Concerns About Accuracy of Emotion AI for Mental Health Assessments
      </Nav.Link>
      {/* <Nav.Link as={Link} to="/scenario4" className="text-dark">
        4 <b>Video Company</b> - Ask for Suggestion for Applied Emotion AI in Our Real-Time Emotion Tracking
      </Nav.Link>
      <Nav.Link as={Link} to="/scenario5" className="text-dark">
        5 <b>School</b> - Emotion AI Solutions for Enhancing Classroom Management and Student Well-being
      </Nav.Link>
      <Nav.Link as={Link} to="/scenario6" className="text-dark">
        6 <b>UX Research Team</b> - Inquiry About Emotion AI for User Interaction Analysis and Persona
      </Nav.Link> */}
    </Nav>
  );
}

export default Sidebar;
