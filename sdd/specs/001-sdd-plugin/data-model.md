# Data Model

## Plugin Architecture Data Model

### Plugin Configuration Structure

#### Plugin Manifest
```json
{
  "name": "sdd",
  "displayName": "Spec-Driven Development",
  "description": "Transform ideas into structured specifications and executable code through systematic workflow",
  "version": "1.0.0",
  "author": "Thierry Lemaire",
  "license": "MIT",
  "repository": "https://github.com/tlemaire/marketplace",
  "keywords": ["specification", "planning", "development", "workflow", "claude-code"],
  "commands": "./commands",
  "dependencies": [],
  "claudeCode": {
    "minVersion": "2.0.37",
    "features": ["slash-commands", "file-operations", "context-management", "git-integration"]
  }
}
```

### Command Structure
```yaml
# Command Template (commands/command.md)
---
description: Brief description of command purpose
shortcut: sdd.command_name
parameters:
  - name: "parameter_name"
    type: "string|boolean|array"
    required: true|false
    description: "Parameter description"
examples:
  - usage: "/sdd.command_name example"
    description: "Example usage description"
  - usage: "/sdd.command_name example with options"
    description: "Another example with options"
---

# Command implementation details
```

### Command Configuration
```typescript
interface CommandConfig {
  name: string;
  description: string;
  shortcut: string;
  parameters?: Parameter[];
  examples?: CommandExample[];
  version?: string;
  deprecated?: boolean;
  category?: string;
}

interface Parameter {
  name: string;
  type: 'string' | 'boolean' | 'array' | 'object';
  required: boolean;
  description: string;
  default?: any;
  validation?: ValidationRule[];
}

interface CommandExample {
  usage: string;
  description: string;
  parameters?: Record<string, any>;
  expectedOutput?: string;
}
```

## Project Data Structures

### Project Memory Structure
```typescript
interface ProjectMemory {
  project: {
    id: string;
    name: string;
    path: string;
    createdAt: Date;
    updatedAt: Date;
  };
  constitution: {
    version: string;
    principles: string[];
    qualityStandards: QualityStandards;
    decisionFramework: DecisionFramework;
  };
  features: Feature[];
  context: ProjectContext;
}

interface QualityStandards {
  codeQuality: CodeQualityStandards;
  userExperience: UserExperienceStandards;
  performance: PerformanceStandards;
  security: SecurityStandards;
  documentation: DocumentationStandards;
}

interface Feature {
  id: string;
  name: string;
  description: string;
  status: 'planning' | 'in-progress' | 'completed' | 'archived';
  createdAt: Date;
  updatedAt: Date;
  specifications: Specification[];
  plans: Plan[];
  tasks: Task[];
  checklists: Checklist[];
}

interface ProjectContext {
  currentWorkingDirectory: string;
  gitBranch: string;
  lastCommand: string;
  sessionState: Record<string, any>;
  userPreferences: UserPreferences;
}
```

### Specification Data Model
```typescript
interface Specification {
  id: string;
  title: string;
  description: string;
  version: string;
  status: 'draft' | 'review' | 'approved';
  createdAt: Date;
  updatedAt: Date;

  // Content sections
  projectOverview: ProjectOverview;
  userStories: UserStory[];
  functionalRequirements: FunctionalRequirement[];
  nonFunctionalRequirements: NonFunctionalRequirement[];
  technicalConstraints: TechnicalConstraint[];
  successMetrics: SuccessMetric[];
  acceptanceCriteria: AcceptanceCriteria[];

  // Metadata
  metadata: SpecificationMetadata;
  tags: string[];
  complexity: 'beginner' | 'intermediate' | 'advanced' | 'enterprise';
}

interface UserStory {
  id: string;
  title: string;
  narrative: string;
  acceptanceCriteria: AcceptanceCriteria[];
  priority: 'low' | 'medium' | 'high' | 'critical';
  estimatedEffort: number;
  dependencies: string[];
}

interface FunctionalRequirement {
  id: string;
  description: string;
  category: string;
  priority: 'low' | 'medium' | 'high' | 'critical';
  source: 'user-story' | 'stakeholder' | 'technical';
  validation: string[];
}
```

### Planning Data Model
```typescript
interface Plan {
  id: string;
  specificationId: string;
  title: string;
  description: string;
  version: string;
  createdAt: Date;
  updatedAt: Date;

  // Architecture sections
  architecture: ArchitectureOverview;
  technologyStack: TechnologyStack;
  dataModel: DataModelOverview;
  apiDesign: APIDesign;
  componentStructure: ComponentStructure;
  implementationApproach: ImplementationApproach;

  // Environment and deployment
  environmentConfiguration: EnvironmentConfiguration;
  deploymentStrategy: DeploymentStrategy;
  developmentWorkflow: DevelopmentWorkflow;

  // Quality considerations
  performanceConsiderations: PerformanceConsiderations;
  securityImplementation: SecurityImplementation;
  testingStrategy: TestingStrategy;
  riskAssessment: RiskAssessment;
}

interface ArchitectureOverview {
  style: string;
  components: Component[];
  relationships: Relationship[];
  patterns: ArchitecturePattern[];
  tradeoffs: Tradeoff[];
}

interface TechnologyStack {
  frontend: Technology[];
  backend: Technology[];
  database: DatabaseTechnology[];
  infrastructure: InfrastructureTechnology[];
  developmentTools: DevelopmentTool[];
}

interface Technology {
  name: string;
  version: string;
  category: string;
  purpose: string;
  alternatives: Alternative[];
  selectionRationale: string;
}
```

### Task Management Data Model
```typescript
interface Task {
  id: string;
  specificationId: string;
  planId: string;
  title: string;
  description: string;
  type: 'development' | 'testing' | 'documentation' | 'deployment';
  status: 'todo' | 'in-progress' | 'done' | 'blocked';
  priority: 'low' | 'medium' | 'high' | 'critical';
  estimatedEffort: number;
  actualEffort?: number;

  // Dependencies
  dependencies: TaskDependency[];
  dependents: TaskDependency[];

  // Content
  acceptanceCriteria: AcceptanceCriteria[];
  testingRequirements: TestingRequirement[];
  implementationNotes: string;

  // Tracking
  createdAt: Date;
  updatedAt: Date;
  startedAt?: Date;
  completedAt?: Date;
  assignedTo?: string;

  // File associations
  files: TaskFile[];
}

interface TaskDependency {
  taskId: string;
  type: 'blocks' | 'depends_on' | 'related';
  description: string;
}

interface TaskFile {
  path: string;
  type: 'create' | 'modify' | 'delete' | 'review';
  description: string;
  content?: string;
}
```

### Quality Assurance Data Model
```typescript
interface Checklist {
  id: string;
  projectId: string;
  featureId: string;
  type: 'requirements' | 'ux' | 'performance' | 'accessibility' | 'security';
  title: string;
  description: string;
  version: string;
  createdAt: Date;
  updatedAt: Date;

  items: ChecklistItem[];
  sections: ChecklistSection[];
  results: ChecklistResult[];
}

interface ChecklistItem {
  id: string;
  category: string;
  description: string;
  type: 'checklist' | 'validation' | 'verification';
  required: boolean;
  evidence: string;
  status: 'pending' | 'passed' | 'failed' | 'not-applicable';
  notes?: string;
  testedAt?: Date;
  testedBy?: string;
}

interface ChecklistResult {
  checklistId: string;
  overallScore: number;
  completedItems: number;
  totalItems: number;
  passedItems: number;
  failedItems: number;
  blockedItems: number;
  testedAt: Date;
  testedBy: string;
  recommendations: string[];
  criticalIssues: string[];
}
```

## User Interface Data Models

### User Preferences
```typescript
interface UserPreferences {
  sdd: SDDUserPreferences;
  ui: UIPreferences;
  privacy: PrivacyPreferences;
  notifications: NotificationPreferences;
}

interface SDDUserPreferences {
  complexityLevel: 'beginner' | 'intermediate' | 'advanced' | 'enterprise';
  autoSave: boolean;
  autoBackup: boolean;
  templateStyle: 'detailed' | 'concise' | 'technical';
  language: string;
  timezone: string;
  defaultTemplates: TemplatePreferences;
}

interface TemplatePreferences {
  constitution: string;
  specification: string;
  plan: string;
  tasks: string;
  checklist: string;
}
```

### Session Management
```typescript
interface Session {
  id: string;
  userId?: string;
  projectPath: string;
  startTime: Date;
  lastActivity: Date;
  context: SessionContext;
  state: SessionState;
}

interface SessionContext {
  currentProject: string;
  currentFeature: string;
  lastCommand: string;
  commandHistory: CommandHistory[];
  workingDirectory: string;
  gitBranch: string;
  environment: EnvironmentContext;
}

interface SessionState {
  projectState: ProjectState;
  commandState: CommandState;
  generationProgress: GenerationProgress;
  validationResults: ValidationResult[];
}
```

## Template System Data Models

### Template Structure
```typescript
interface Template {
  id: string;
  name: string;
  description: string;
  category: 'constitution' | 'specification' | 'plan' | 'tasks' | 'checklist';
  type: string;
  complexity: 'beginner' | 'intermediate' | 'advanced' | 'enterprise';
  language: string;

  // Template content
  content: string;
  variables: TemplateVariable[];
  sections: TemplateSection[];

  // Metadata
  version: string;
  createdAt: Date;
  updatedAt: Date;
  author: string;
  tags: string[];
  usage: number;
}

interface TemplateVariable {
  name: string;
  type: 'string' | 'number' | 'boolean' | 'array' | 'object';
  description: string;
  required: boolean;
  default?: any;
  validation?: ValidationRule[];
  options?: any[];
}

interface TemplateSection {
  id: string;
  name: string;
  description: string;
  required: boolean;
  variables: string[];
  content: string;
  conditional?: ConditionalSection;
}
```

### Validation Data Models
```typescript
interface ValidationRule {
  type: 'required' | 'pattern' | 'length' | 'range' | 'custom';
  constraint: any;
  message: string;
  severity: 'error' | 'warning' | 'info';
}

interface ValidationResult {
  isValid: boolean;
  errors: ValidationError[];
  warnings: ValidationWarning[];
  score: number;
  recommendations: string[];
}

interface ValidationError {
  field: string;
  message: string;
  value: any;
  rule: ValidationRule;
}

interface ValidationWarning {
  field: string;
  message: string;
  value: any;
  recommendation: string;
}
```

## File System Data Models

### File Structure
```typescript
interface ProjectStructure {
  root: string;
  name: string;
  directories: Directory[];
  files: FileNode[];
}

interface Directory {
  path: string;
  name: string;
  type: 'specs' | 'src' | 'docs' | 'config' | 'assets' | 'tests';
  children: FileNode[];
  description: string;
}

interface FileNode {
  path: string;
  name: string;
  type: 'file';
  content?: string;
  description: string;
  contentType: 'specification' | 'plan' | 'tasks' | 'checklist' | 'documentation' | 'configuration';
  size?: number;
  created?: boolean;
  modified?: boolean;
}
```

### Content Generation
```typescript
interface GeneratedContent {
  id: string;
  templateId: string;
  type: 'specification' | 'plan' | 'tasks' | 'checklist';
  name: string;
  path: string;
  content: string;
  metadata: ContentMetadata;
}

interface ContentMetadata {
  generatedAt: Date;
  template: string;
  version: string;
  variables: Record<string, any>;
  quality: QualityScore;
  size: number;
  checksum: string;
}
```

This comprehensive data model provides the foundation for implementing a robust, scalable, and maintainable SDD plugin with proper data organization, type safety, and extensibility for future enhancements.