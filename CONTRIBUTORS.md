# Contributing to Edunova ERP

We love your input! We want to make contributing to Edunova ERP as easy and transparent as possible.

## Development Process

1. Fork this template in Replit
2. Make your changes
3. If you've added code that should be tested, add tests
4. If you've changed APIs, update the documentation
5. Ensure the test suite passes
6. Issue that pull request!

## Development Setup

1. **Install Dependencies**
   ```bash
   npm install
   ```

2. **Environment Variables**
   Create a `.env` file based on `.env.example`:
   ```
   DATABASE_URL=postgresql://user:password@localhost:5432/school_erp
   SESSION_SECRET=your_secure_session_secret
   ```

3. **Database Setup**
   ```bash
   npm run db:push
   ```

4. **Start Development Server**
   ```bash
   npm run dev
   ```

## Coding Style

* 2 spaces for indentation rather than tabs
* 80 character line length
* Run `npm run lint` to ensure your code follows our style

### TypeScript Guidelines
- Use TypeScript for all new code
- Define interfaces for all data structures
- Use proper type annotations
- Avoid using `any` type

### React Guidelines
- Use functional components with hooks
- Follow the container/presentational pattern
- Use proper prop types
- Keep components small and focused

### API Guidelines
- RESTful endpoints should use proper HTTP methods
- Include proper error handling
- Document all endpoints
- Use proper status codes

## Report Bugs

Report a bug by opening a new issue in the repository.

## Write Bug Reports with Detail

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening)

## License

By contributing, you agree that your contributions will be licensed under its MIT License.
