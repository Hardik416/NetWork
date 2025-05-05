// DOM Elements
const darkModeToggle = document.getElementById('darkMode');
const body = document.body;
const profileForm = document.getElementById('profileForm');

// Add Experience Button
const addExperienceBtn = document.getElementById('addExperience');
const experienceContainer = document.getElementById('experienceContainer');

// Add Education Button
const addEducationBtn = document.getElementById('addEducation');
const educationContainer = document.getElementById('educationContainer');

// Add Top Skill Button
const addTopSkillBtn = document.getElementById('addSkill');
const topSkillsContainer = document.getElementById('skillsContainer');

// Add Certification Button
const addCertificationBtn = document.getElementById('addCertification');
const certificationsContainer = document.getElementById('certificationsContainer');

// Add Language Button
const addLanguageBtn = document.getElementById('addLanguage');
const languagesContainer = document.getElementById('languagesContainer');

// Other Skills Tags Input
const skillInput = document.getElementById('skillInput');
const otherSkillsContainer = document.getElementById('otherSkillsContainer');

// Toggle Dark Mode
darkModeToggle.addEventListener('change', () => {
  body.classList.toggle('dark-mode');
  
  // Save preference to localStorage
  if (body.classList.contains('dark-mode')) {
    localStorage.setItem('darkMode', 'enabled');
  } else {
    localStorage.setItem('darkMode', 'disabled');
  }
});

// Check for saved theme preference
if (localStorage.getItem('darkMode') === 'enabled') {
  body.classList.add('dark-mode');
  darkModeToggle.checked = true;
}

// Add Experience Section
addExperienceBtn.addEventListener('click', () => {
  const newExperience = document.createElement('div');
  newExperience.className = 'section-item';
  newExperience.innerHTML = `
    <button type="button" class="remove-btn">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <line x1="18" y1="6" x2="6" y2="18"></line>
        <line x1="6" y1="6" x2="18" y2="18"></line>
      </svg>
    </button>
    
    <div class="form-group">
      <label class="form-label">Job Title*</label>
      <input type="text" class="form-input" name="experienceTitle[]" required>
    </div>
    
    <div class="form-group">
      <label class="form-label">Company*</label>
      <input type="text" class="form-input" name="experienceCompany[]" required>
    </div>
    
    <div class="two-column">
      <div class="column">
        <div class="form-group">
          <label class="form-label">Start Date*</label>
          <input type="number" class="form-input" name="experienceStartYear[]" required>
        </div>
      </div>
      <div class="column">
        <div class="form-group">
          <label class="form-label">End Date</label>
          <input type="number" class="form-input" name="experienceEndYear[]" required>
          <div style="margin-top: 10px;">
            <input type="checkbox" id="currentJob${Date.now()}" name="currentJob[]">
            <label for="currentJob${Date.now()}" style="font-size: 14px; font-weight: normal;">I currently work here</label>
          </div>
        </div>
      </div>
    </div>
  `;
  
  experienceContainer.appendChild(newExperience);
  
  // Add event listener to the new remove button
  const removeBtn = newExperience.querySelector('.remove-btn');
  removeBtn.addEventListener('click', () => {
    experienceContainer.removeChild(newExperience);
  });
});

// Add Education Section
addEducationBtn.addEventListener('click', () => {
  const newEducation = document.createElement('div');
  newEducation.className = 'section-item';
  newEducation.innerHTML = `
    <button type="button" class="remove-btn">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <line x1="18" y1="6" x2="6" y2="18"></line>
        <line x1="6" y1="6" x2="18" y2="18"></line>
      </svg>
    </button>
    
    <div class="form-group">
      <label class="form-label">School/University*</label>
      <input type="text" class="form-input" name="educationSchool[]" required>
    </div>
    
    <div class="form-group">
      <label class="form-label">Degree*</label>
      <input type="text" class="form-input" name="educationDegree[]" placeholder="e.g. Bachelor of Science in Computer Science" required>
    </div>
    
    <div class="two-column">
      <div class="column">
        <div class="form-group">
          <label class="form-label">Start Year*</label>
          <input type="number" class="form-input" name="educationStartYear[]" required>
        </div>
      </div>
      <div class="column">
        <div class="form-group">
          <label class="form-label">End Year (or Expected)*</label>
          <input type="number" class="form-input" name="educationEndYear[]" required>
        </div>
      </div>
    </div>
    
    <div class="form-group">
      <label class="form-label">Field of Study</label>
      <input type="text" class="form-input" name="educationField[]">
    </div>
  `;
  
  educationContainer.appendChild(newEducation);
  
  // Add event listener to the new remove button
  const removeBtn = newEducation.querySelector('.remove-btn');
  removeBtn.addEventListener('click', () => {
    educationContainer.removeChild(newEducation);
  });
});

// Add Top Skill
addTopSkillBtn.addEventListener('click', () => {
  const newSkill = document.createElement('div');
  newSkill.className = 'skill-input-group';
  newSkill.innerHTML = `
    <div class="skill-input">
      <input type="text" class="form-input" name="topSkillName[]" placeholder="Skill name" required>
    </div>
    <div class="level-select">
      <select class="form-select" name="topSkillLevel[]" required>
        <option value="">Proficiency Level</option>
        <option value="Beginner">Beginner</option>
        <option value="Intermediate">Intermediate</option>
        <option value="Advanced">Advanced</option>
        <option value="Expert">Expert</option>
      </select>
    </div>
  `;
  
  topSkillsContainer.appendChild(newSkill);
});

// Add event listeners to existing remove buttons
document.querySelectorAll('.remove-btn').forEach(button => {
  button.addEventListener('click', () => {
    const sectionItem = button.closest('.section-item');
    sectionItem.parentNode.removeChild(sectionItem);
  });
});

// Handle current job checkbox
document.addEventListener('change', (e) => {
  if (e.target && e.target.name === 'currentJob[]') {
    const endDateInput = e.target.closest('.column').querySelector('input[type="month"]');
    endDateInput.disabled = e.target.checked;
    if (e.target.checked) {
      endDateInput.value = '';
    }
  }
  
  if (e.target && e.target.name === 'noExpiry[]') {
    const expiryDateInput = e.target.closest('.column').querySelector('input[type="month"]');
    expiryDateInput.disabled = e.target.checked;
    if (e.target.checked) {
      expiryDateInput.value = '';
    }
  }
});

// Form Validation
profileForm.addEventListener('submit', (e) => {
  // Example: Check if at least one experience is added
  if (experienceContainer.children.length === 0) {
    e.preventDefault();
    alert('Please add at least one experience');
    return;
  }
  
  // Example: Check if at least one education is added
  if (educationContainer.children.length === 0) {
    e.preventDefault();
    alert('Please add at least one education');
    return;
  }
}); 