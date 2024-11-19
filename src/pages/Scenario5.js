import React from 'react';
import { Container, Row, Col, Form, Button } from 'react-bootstrap';

function Scenario5() {
  return (
    <Container className="p-4">
      {/* Email UI */}
      <Row className="border-bottom pb-3 mb-3">
        <Col>
          <h1>Subject: Emotion AI Solutions for Enhancing Classroom Management and Student Well-being</h1>
          <p className="text-muted">From: cjackson2@schoolE.edu</p>
          <p className="text-muted">To: you@emoai.com</p>
        </Col>
      </Row>
      <Row>
        <Col>
          <p>
            Dear Consultant,
            <br />
            <br />
            I hope this email finds you well. My name is Cecile, and I serve as the Education Manager at Center First High School, a high school with a large student body comprising over a thousand students in each grade and more than fifty students per class. With only one teacher per class, we face significant challenges in effectively managing classrooms and addressing the individual needs of our students.
            <br />
            <br />
            To address these challenges, our school is interested in leveraging Emotion AI technologies to:
            <ul>
              <li>Help teachers monitor and manage students' emotions and attention levels during class to ensure effective learning outcomes.</li>
              <li>Identify students who may require additional support due to mental health concerns.</li>
              <li>Assist teachers in creating a more personalized and inclusive learning environment.</li>
            </ul>
            We are considering the use of cameras in classrooms to collect facial data as a means to analyze students' emotional and attentional states. Given your expertise in Emotion AI, we would greatly value your insights on:
            <ul>
              <li>Recommended technologies or solutions that align with our objectives based on your product.</li>
              <li>Advantages and disadvantages if we applied this technology in our school</li>
            </ul>
            Thank you for your time and expertise. We look forward to hearing from you.
            <br />
            <br />
            Best regards,
            <br />
            Cecile Jackson
            <br />
            Education Manager
            <br />
            School E
          </p>
        </Col>
      </Row>
      {/* Reply Section */}
      <Row className="mt-4">
        <Col>
          <Form>
            <Form.Group controlId="replyTextArea">
              <Form.Label>Reply:</Form.Label>
              <Form.Control as="textarea" rows={5} placeholder="Type your reply here..." />
            </Form.Group>
            <Button variant="primary" className="mt-3">Send</Button>
          </Form>
        </Col>
      </Row>
    </Container>
  );
}

export default Scenario5;