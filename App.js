import React, { useState } from 'react';
import { View, TextInput, Button, Text } from 'react-native';

const App = () => {
    const [message, setMessage] = useState('');
    const [response, setResponse] = useState('');

    const sendMessage = () => {
        fetch('http:// 178.131.151.37:5000/send', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message }),
        })
            .then(res => res.json())
            .then(data => setResponse(data.message))
            .catch(err => console.error(err));
    };

    return (
        <View style={{ padding: 20 }}>
            <TextInput
                placeholder="Enter your message"
                value={message}
                onChangeText={setMessage}
                style={{ borderWidth: 1, marginBottom: 10, padding: 8 }}
            />
            <Button title="Send" onPress={sendMessage} />
            <Text style={{ marginTop: 20 }}>Response: {response}</Text>
        </View>
    );
};

export default App;
