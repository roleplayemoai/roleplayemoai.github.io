import React from 'react';
import { Container, Row, Col, Form, Button } from 'react-bootstrap';

function Scenario6() {
  return (
    <Container className="p-4">
      {/* Email UI */}
      <Row className="border-bottom pb-3 mb-3">
        <Col>
          <h1>Subject: Inquiry About Emotion AI for User Interaction Analysis and Persona </h1>
          <p className="text-muted">From: michael.liu@mail.com</p>
          <p className="text-muted">To: you@emoai.com</p>
        </Col>
      </Row>
      <Row>
        <Col>
          <p>
            Dear EmoAI Customer Support Team,
            <br />
            <br />
            I hope this email finds you well. My name is Michael, and I am a User Experience Researcher from the UX research team. We are exploring the potential of Emotion AI to analyze user interactions with our products and refine our user personas.
            <br />
            <br />
            Our primary goal is to track users' emotional responses to better understand their preferences and behavioral patterns. We believe this could offer valuable insights to improve our designs and create more meaningful user experiences.
            <br />
            <br />
            However, I have some concerns about the application of this technology, particularly about overly intrusive profiling and potential stereotyping
            I would greatly appreciate your expert opinion on whether Emotion AI is well-suited to achieving these goals and any advice you have for mitigating these challenges. Additionally, insights into best practices for ethical implementation and examples of successful applications would be extremely helpful.
            <br />
            <br />
            If you are available, I'd love to schedule a time to discuss this in more detail. Thank you for your time and expertise, and I look forward to your response.
            <br />
            <br />
            Best regards,
            <br />
            Michael Liu
            <br />
            User Experience Researcher
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

export default Scenario6;