// To musi być w Twoim pliku index.js lub app.js na serwerze
app.get('/ping', (req, res) => {
    res.status(200).send('pong');
});
