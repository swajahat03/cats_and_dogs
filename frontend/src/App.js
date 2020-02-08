import React from 'react';
import { Card, Row, Col } from "antd";
import "antd/dist/antd.css";
import './App.css';
import kitten1 from './resources/kitten1.jpg';
import kitten2 from './resources/kitten2.jpg';
import kitten3 from './resources/kitten3.jpeg';
import puppy1 from './resources/puppy1.jpeg';
import puppy2 from './resources/puppy2.jpg';
import puppy3 from './resources/puppy3.jpg';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p style={{margin: 30}}>
          Choose your favorite animal!
        </p>
      <div >
        <Row gutter={16}>
          <Col span={8}>
            <Card title="kitten1" style={{ margin: 30, height: 300, width: 300}}>
              <img src={kitten1} alt="Kitten1" style={{width: 250}}></img>
            </Card>
          </Col>
          <Col span={8}>
            <Card title="puppy1" style={{ margin: 30, height: 300, width: 300}}>
              <img src={puppy1} alt="Puppy1" style={{width: 250}}></img>
            </Card>
          </Col>
          <Col span={8}>
            <Card title="kitten2" style={{ margin: 30, height: 300, width: 300}}>
              <img src={kitten2} alt="Kitten2" style={{width: 250}}></img>
            </Card>
          </Col>
          
        </Row>
        
        <Row gutter={16}>
          <Col span={8}>
            <Card title="puppy2" style={{ margin: 30, height: 300, width: 300}}>
              <img src={puppy2} alt="Puppy2" style={{width: 250}}></img>  
            </Card>
          </Col>
          <Col span={8}>
            <Card title="kitten3" style={{ margin: 30, height: 300, width: 300}}>
              <img src={kitten3} alt="Kitten3" style={{width: 250}}></img>
            </Card>
          </Col>
          <Col span={8}>
            <Card title="puppy3" style={{ margin: 30, height: 300, width: 300}}>
              <img src={puppy3} alt="Puppy3" style={{width: 250}}></img>
            </Card>
          </Col>
          
        </Row>
        
      </div>
      
      </header>
      
    </div>
  );
}

export default App;
