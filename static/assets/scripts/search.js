const searchBar = document.getElementById('searchBar');
const papersList = document.getElementById('papersList');
const papers = Array.from(papersList.getElementsByTagName('li'));

searchBar.addEventListener('input', () => {
    const filter = searchBar.value.toLowerCase();
    let exactMatchFound = false;

    papers.forEach(paper => {
        const text = paper.textContent.toLowerCase();
        if (text === filter && filter !== '') {
            exactMatchFound = true;
            paper.style.display = ''; // Show only the exact match
        } else if (!exactMatchFound && text.includes(filter)) {
            paper.style.display = ''; // Show items that match the filter
        } else {
            paper.style.display = 'none'; // Hide non-matching items
        }
    });
});
